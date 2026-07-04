from src.models import Contribution


def get_contribution(month: int) -> Contribution:

    if month <= 36:

        return Contribution(
            ceiling=45000,
            salary=24845
        )

    elif month <= 72:

        return Contribution(
            ceiling=80000,
            salary=40000
        )

    return Contribution(
        ceiling=80000,
        salary=50000
    )