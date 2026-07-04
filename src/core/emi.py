from math import pow


class EMIEngine:
    """
    Calculates EMI for a loan.
    """

    @staticmethod
    def calculate(
        principal: float,
        annual_rate: float,
        months: int,
    ) -> float:

        if principal <= 0:
            return 0.0

        monthly_rate = annual_rate / 12

        if monthly_rate == 0:
            return principal / months

        factor = pow(1 + monthly_rate, months)

        return (
            principal
            * monthly_rate
            * factor
            / (factor - 1)
        )