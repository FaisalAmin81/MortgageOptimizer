from dataclasses import dataclass, field

from src.models.settlement import Settlement


@dataclass
class SettlementHistory:
    """
    Stores every settlement made during the simulation.
    """

    settlements: list[Settlement] = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.settlements)

    @property
    def last(self) -> Settlement | None:
        if not self.settlements:
            return None
        return self.settlements[-1]
