from src.core.emi import EMIEngine
from src.models.mortgage_context import MortgageContext
from src.models.settlement import Settlement
from src.services.savings_service import SavingsService


class SettlementService:
    """
    Executes a mortgage settlement.
    """

    @staticmethod
    def apply(
        context: MortgageContext,
    ) -> bool:

        state = context.state
        loan = context.loan
        savings = context.savings
        rule = context.settlement_rule
        history = context.settlement_history

        settlement_amount = savings.balance

        # Nothing to settle
        if settlement_amount <= 0:
            return False

        # Store values before settlement
        balance_before = state.balance
        emi_before = state.current_emi

        # Withdraw all savings
        SavingsService.withdraw(
            savings=savings,
            month=state.current_month,
            description="Mortgage Settlement",
            amount=settlement_amount,
        )

        # Reduce loan balance
        state.balance -= settlement_amount

        if state.balance < 0:
            state.balance = 0

        # Recalculate EMI
        if rule.reduce_emi and state.balance > 0:

            state.current_emi = EMIEngine.calculate(
                principal=state.balance,
                annual_rate=loan.annual_rate,
                months=state.remaining_months,
            )

        else:

            state.current_emi = 0

        balance_after = state.balance
        emi_after = state.current_emi

        # Save settlement history
        history.settlements.append(
            Settlement(
                number=history.count + 1,
                month=state.current_month,
                amount=settlement_amount,
                balance_before=balance_before,
                balance_after=balance_after,
                emi_before=emi_before,
                emi_after=emi_after,
                remaining_months=state.remaining_months,
            )
        )

        return True
