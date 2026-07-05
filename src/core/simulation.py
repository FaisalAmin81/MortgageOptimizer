from src.core.amortization import AmortizationEngine
from src.factories.snapshot_factory import SnapshotFactory
from src.models.mortgage_context import MortgageContext
from src.models.payment import Payment
from src.models.simulation_result import SimulationResult
from src.optimizer.decision_engine import DecisionEngine
from src.optimizer.optimization_policy import OptimizationPolicy
from src.services.contribution_service import ContributionService
from src.services.savings_service import SavingsService
from src.services.settlement_service import SettlementService


class SimulationEngine:
    """
    Runs the complete mortgage simulation.
    """

    @staticmethod
    def run(
        context: MortgageContext,
    ) -> SimulationResult:

        schedule: list[Payment] = []

        policy = OptimizationPolicy()

        while context.state.balance > 0:

            # --------------------------------------------------
            # Step 1 : Process mortgage payment
            # --------------------------------------------------

            payment = AmortizationEngine.process_month(
                context.state,
                context.loan,
            )

            schedule.append(payment)

            # --------------------------------------------------
            # Step 2 : Monthly contribution
            # --------------------------------------------------

            contribution = ContributionService.get(
                context.state.current_month,
            )

            surplus = max(
                contribution.total - context.state.current_emi,
                0,
            )

            # --------------------------------------------------
            # Step 3 : Deposit savings
            # --------------------------------------------------

            if surplus > 0:

                SavingsService.deposit(
                    savings=context.savings,
                    month=context.state.current_month,
                    description="Monthly Surplus",
                    amount=surplus,
                )

            # --------------------------------------------------
            # Step 4 : Settlement decision
            # --------------------------------------------------

            settlement_executed = False
            settlement_amount = 0.0

            if DecisionEngine.should_settle(
                context,
                policy,
            ):

                settlement_amount = context.savings.balance

                SettlementService.apply(context)

                settlement_executed = True

            # --------------------------------------------------
            # Step 5 : Snapshot
            # --------------------------------------------------

            snapshot = SnapshotFactory.create(
                payment=payment,
                state=context.state,
                contribution=contribution,
                savings=context.savings,
                surplus=surplus,
                settlement_amount=settlement_amount,
                settlement_executed=settlement_executed,
            )

            context.monthly_snapshots.append(snapshot)

        # --------------------------------------------------
        # Step 6 : Return result
        # --------------------------------------------------

        return SimulationResult(
            loan=context.loan,
            final_state=context.state,
            payments=schedule,
            snapshots=context.monthly_snapshots,
            savings=context.savings,
            settlement_history=context.settlement_history,
        )
