from dataclasses import dataclass


@dataclass(frozen=True)
class ContributionPeriod:
    start_month: int
    end_month: int | None
    ceiling: float
    salary: float


CONTRIBUTION_SCHEDULE = [
    ContributionPeriod(
        start_month=1,
        end_month=36,
        ceiling=45000,
        salary=24845,
    ),
    ContributionPeriod(
        start_month=37,
        end_month=72,
        ceiling=80000,
        salary=40000,
    ),
    ContributionPeriod(
        start_month=73,
        end_month=None,
        ceiling=80000,
        salary=50000,
    ),
]