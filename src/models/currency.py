from dataclasses import dataclass


@dataclass(frozen=True)
class Currency:
    code: str
    symbol: str
    decimal_places: int = 2