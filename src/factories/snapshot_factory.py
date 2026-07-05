from src.models.contribution import Contribution
from src.models.loan_state import LoanState
from src.models.monthly_snapshot import MonthlySnapshot
from src.models.payment import Payment
from src.models.savings import Savings


class SnapshotFactory:
    """
    Creates a MonthlySnapshot from the current simulation state.
    """

    @staticmethod
    def create(
        *,
        payment: Payment,
        state: LoanState,
        contribution: Contribution,
        savings: Savings,
        surplus: float,
        settlement_amount: float,
        settlement_executed: bool,
    ) -> MonthlySnapshot:

        return MonthlySnapshot(
            month=payment.month,
            opening_balance=payment.opening_balance,
            emi=payment.emi,
            interest=payment.interest,
            principal=payment.principal,
            closing_balance=state.balance,
            ceiling_contribution=contribution.ceiling,
            salary_contribution=contribution.salary,
            total_contribution=contribution.total,
            surplus=surplus,
            savings_balance=savings.balance,
            settlement_amount=settlement_amount,
            settlement_executed=settlement_executed,
            cumulative_interest=state.total_interest_paid,
            cumulative_principal=state.total_principal_paid,
        )
