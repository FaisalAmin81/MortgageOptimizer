from dataclasses import dataclass

from src.models.loan import Loan
from src.models.loan_state import LoanState
from src.models.monthly_snapshot import MonthlySnapshot
from src.models.payment import Payment
from src.models.savings import Savings
from src.models.settlement_history import SettlementHistory


@dataclass
class SimulationResult:
    """
    Complete output of one mortgage simulation.
    """

    loan: Loan

    final_state: LoanState

    payments: list[Payment]

    snapshots: list[MonthlySnapshot]

    savings: Savings

    settlement_history: SettlementHistory

    @property
    def months(self) -> int:
        return len(self.payments)

    @property
    def total_interest(self) -> float:
        return self.final_state.total_interest_paid

    @property
    def total_principal(self) -> float:
        return self.final_state.total_principal_paid

    @property
    def settlements(self) -> int:
        return self.settlement_history.count
