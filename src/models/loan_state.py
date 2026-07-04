from dataclasses import dataclass
from src.models.loan import Loan


@dataclass
class LoanState:
    """
    Represents the current state of a loan during simulation.
    """

    current_month: int

    balance: float

    current_emi: float

    remaining_months: int

    total_interest_paid: float = 0.0

    total_principal_paid: float = 0.0

    @classmethod
    def from_loan(cls, loan: Loan):

         return cls(
         current_month=0,
         balance=loan.principal,
         current_emi=loan.emi,
         remaining_months=loan.term_months,

    )