from dataclasses import dataclass


@dataclass(frozen=True)
class SettlementConfig:

    minimum_amount: float

    maximum_settlements: int