from src.core.amortization import AmortizationEngine
from src.models.mortgage_context import MortgageContext
from src.models.payment import Payment
from src.services.contribution_service import ContributionService
from src.services.savings_service import SavingsService
from src.services.settlement_service import SettlementService


class SimulationEngine:
    """
    Runs the month-by-month mortgage simulation.
    """

    @staticmethod
    def run(
        context: MortgageContext,
    ) -> list[Payment]:

        schedule: list[Payment] = []

        while context.state.balance > 0:

            payment = AmortizationEngine.process_month(
                context.state,
                context.loan,
            )

            schedule.append(payment)
            contribution = ContributionService.get(
                context.state.current_month,
            )
            surplus = contribution.total - context.state.current_emi
            if surplus > 0:
                SavingsService.deposit(
                    savings=context.savings,
                    month=context.state.current_month,
                    description="Monthly Surplus",
                    amount=surplus,
                )
                SettlementService.apply(context)

        return schedule
