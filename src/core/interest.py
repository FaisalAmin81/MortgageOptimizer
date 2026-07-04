from abc import ABC, abstractmethod


class InterestEngine(ABC):
    """
    Base class for all interest calculation engines.

    Different banks use different interest calculation methods.
    Subclasses should implement the `calculate` method.
    """

    @staticmethod
    @abstractmethod
    def calculate(
        balance: float,
        annual_rate: float,
    ) -> float:
        """
        Calculate the interest for the current period.

        Args:
            balance: Outstanding loan balance.
            annual_rate: Annual interest rate (e.g. 0.05 for 5%).

        Returns:
            Interest amount for the period.
        """
        raise NotImplementedError