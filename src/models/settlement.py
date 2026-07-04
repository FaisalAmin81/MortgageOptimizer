from dataclasses import dataclass


@dataclass
class Settlement:
    """
    Represents one mortgage settlement event.
    """

    number: int

    month: int

    amount: float

    balance_before: float

    balance_after: float

    emi_before: float

    emi_after: float

    remaining_months: int

    interest_saved_estimate: float | None = None
