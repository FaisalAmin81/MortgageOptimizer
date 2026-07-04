from calendar import month
from multiprocessing import context

from src.core.amortization import AmortizationEngine
from src.models.monthly_snapshot import MonthlySnapshot
from src.models.mortgage_context import MortgageContext
from src.models.payment import Payment
from src.services.contribution_service import ContributionService
from src.services.savings_service import SavingsService
from src.services.settlement_service import SettlementService
from src.optimizer.decision_engine import DecisionEngine
from src.optimizer.optimization_policy import OptimizationPolicy
from src.services.settlement_service import SettlementService


class SimulationEngine:
    """
    Runs the month-by-month mortgage simulation.
    """

    policy = OptimizationPolicy()
    settlement_executed: bool = False

    @staticmethod
    def run(
        context: MortgageContext,
    ) -> list[Payment]:

        schedule: list[Payment] = []
        policy = OptimizationPolicy()

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
                if DecisionEngine.should_settle(
                    context,
                    policy,
                ):
                    SettlementService.apply(context)

                    snapshot = MonthlySnapshot(
                        month=payment.month,
                        opening_balance=payment.opening_balance,
                        emi=payment.emi,
                        interest=payment.interest,
                        principal=payment.principal,
                        closing_balance=context.state.balance,
                        ceiling_contribution=contribution.ceiling,
                        salary_contribution=contribution.salary,
                        total_contribution=contribution.total,
                        surplus=surplus,
                        savings_balance=context.savings.balance,
                        cumulative_interest=context.state.total_interest_paid,
                        cumulative_principal=context.state.total_principal_paid,
                    )
                    context.monthly_snapshots.append(snapshot)

                    for month in context.monthly_snapshots:
                        print(month)

        return schedule
