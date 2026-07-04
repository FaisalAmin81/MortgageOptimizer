from dataclasses import dataclass


@dataclass
class ScenarioResult:

    payoff_month: int

    total_interest: float

    interest_saved: float

    remaining_savings: float

    settlements_used: int
    