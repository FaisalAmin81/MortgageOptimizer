from src.core.monthly_interest import MonthlyInterestEngine
from src.models.loan import Loan
from src.models.loan_state import LoanState
from src.models.payment import Payment


class AmortizationEngine:
    """
    Processes exactly ONE month of the loan.
    """

    @staticmethod
    def process_month(
        state: LoanState,
        loan: Loan,
    ) -> Payment:

        opening_balance = state.balance

        interest = MonthlyInterestEngine.calculate(
            balance=opening_balance,
            annual_rate=loan.annual_rate,
        )

        principal = state.current_emi - interest

        # Prevent overpayment in final month
        if principal > opening_balance:
            principal = opening_balance
            emi = interest + principal
        else:
            emi = state.current_emi

        closing_balance = opening_balance - principal

        payment = Payment(
            month=state.current_month + 1,
            opening_balance=opening_balance,
            emi=emi,
            interest=interest,
            principal=principal,
            closing_balance=closing_balance,
        )

        # Update loan state
        state.balance = closing_balance
        state.current_month += 1
        state.remaining_months -= 1
        state.total_interest_paid += interest
        state.total_principal_paid += principal
        state.current_emi = emi

        return payment