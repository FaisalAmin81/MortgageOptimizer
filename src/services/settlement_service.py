from src.core.emi import EMIEngine
from src.models.loan import Loan
from src.models.loan_state import LoanState
from src.models.savings import Savings
from src.models.settlement import Settlement
from src.models.settlement_history import SettlementHistory
from src.models.settlement_rule import SettlementRule
from src.services.savings_service import SavingsService
from src.models.mortgage_context import MortgageContext



class SettlementService:

    @staticmethod
    def apply(
        context: MortgageContext
    )-> bool:
        loan = context.loan
        state = context.state
        savings = context.savings
        history = context.settlement_history
        rule = context.settlement_rule

         
        """
        Apply a settlement if savings meet the minimum requirement.

        Returns:
            True if a settlement was applied.
            False otherwise.
        """

        # Not enough savings
        if savings.balance < rule.minimum_amount:
            return False

        settlement_amount = savings.balance

        # Store values before settlement
        balance_before = state.balance
        emi_before = state.current_emi

        # Withdraw from savings
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

        # Record settlement
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