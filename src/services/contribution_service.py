from src.config.contribution_config import CONTRIBUTION_SCHEDULE
from src.models.contribution import Contribution


class ContributionService:

    @staticmethod
    def get(month: int) -> Contribution:

        for period in CONTRIBUTION_SCHEDULE:

            if period.end_month is None:

                if month >= period.start_month:

                    return Contribution(

                        ceiling=period.ceiling,

                        salary=period.salary

                    )

            elif period.start_month <= month <= period.end_month:

                return Contribution(

                    ceiling=period.ceiling,

                    salary=period.salary

                )

        raise ValueError(f"No contribution configured for month {month}")