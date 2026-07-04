from src.core.amortization import AmortizationEngine
from src.models.loan import Loan
from src.models.loan_state import LoanState
from src.models.payment import Payment


class SimulationEngine:
    """
    Runs the month-by-month mortgage simulation.
    """

    @staticmethod
    def run(
        state: LoanState,
        loan: Loan,
    ) -> list[Payment]:

        schedule: list[Payment] = []

        while state.balance > 0:

            payment = AmortizationEngine.process_month(
                state,
                loan,
            )

            schedule.append(payment)

        return schedule