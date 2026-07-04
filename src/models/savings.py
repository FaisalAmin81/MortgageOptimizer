from dataclasses import dataclass, field

from src.models.transaction import Transaction


@dataclass
class Savings:

    balance: float = 0.0

    transactions: list[Transaction] = field(default_factory=list)