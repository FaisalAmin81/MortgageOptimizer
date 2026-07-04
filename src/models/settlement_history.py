from dataclasses import dataclass, field

from src.models.settlement import Settlement


@dataclass
class SettlementHistory:

    settlements: list[Settlement] = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.settlements)

    @property
    def total_amount(self) -> float:
        return sum(s.amount for s in self.settlements)