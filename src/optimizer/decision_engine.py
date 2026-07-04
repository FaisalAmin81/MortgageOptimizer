from src.models.mortgage_context import MortgageContext
from src.optimizer.optimization_policy import OptimizationPolicy


class DecisionEngine:
    """
    Decides whether a settlement should occur.
    """

    @staticmethod
    def should_settle(
        context: MortgageContext,
        policy: OptimizationPolicy,
    ) -> bool:

        state = context.state
        savings = context.savings
        history = context.settlement_history

        # Rule 1
        if history.count >= policy.max_settlements:
            return False

        # Rule 2
        if state.current_month < policy.earliest_settlement_month:
            return False

        # Rule 3
        if savings.balance < policy.minimum_settlement:
            return False

        return True
