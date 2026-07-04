from dataclasses import dataclass, field
from src.models.mortgage_context import MortgageContext
from src.models.payment import Payment


@dataclass
class SimulationResult:
    """
    Contains the complete result of one mortgage simulation.
    """

    context: MortgageContext

    payments: list[Payment] = field(default_factory=list)

    @property
    def total_interest(self) -> float:
        return self.context.state.total_interest_paid

    @property
    def total_principal(self) -> float:
        return self.context.state.total_principal_paid

    @property
    def total_settlements(self) -> int:
        return self.context.settlement_history.count

    @property
    def payoff_month(self) -> int:
        return self.context.state.current_month