from dataclasses import dataclass


@dataclass
class Contribution:
    """
    Represents the monthly contribution from all income sources.
    """

    ceiling: float
    salary: float

    @property
    def total(self) -> float:
        return self.ceiling + self.salary