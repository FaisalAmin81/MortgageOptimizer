from src.core.interest import InterestEngine
class DailyInterestEngine(InterestEngine):

    @staticmethod
    def calculate(
        balance: float,
        annual_rate: float,
        days: int = 30,
    ) -> float:

        daily_rate = annual_rate / 365

        return balance * daily_rate * days