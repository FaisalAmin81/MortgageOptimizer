from src.core.interest import InterestEngine


class MonthlyInterestEngine(InterestEngine):
    """
    Standard monthly interest calculation.

    Formula:
        Interest = Balance × (Annual Rate / 12)
    """

    @staticmethod
    def calculate(
        balance: float,
        annual_rate: float,
    ) -> float:

        monthly_rate = annual_rate / 12

        return balance * monthly_rate
    