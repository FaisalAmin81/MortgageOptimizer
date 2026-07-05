from src.models.simulation_result import SimulationResult


class StatisticsService:
    """
    Computes summary statistics from a completed simulation.
    """

    @staticmethod
    def total_interest(result: SimulationResult) -> float:
        return result.final_state.total_interest_paid

    @staticmethod
    def total_principal(result: SimulationResult) -> float:
        return result.final_state.total_principal_paid

    @staticmethod
    def total_months(result: SimulationResult) -> int:
        return len(result.payments)

    @staticmethod
    def total_settlements(result: SimulationResult) -> int:
        return result.settlement_history.count

    @staticmethod
    def total_savings(result: SimulationResult) -> float:
        return result.savings.balance

    @staticmethod
    def final_balance(result: SimulationResult) -> float:
        return result.final_state.balance

    @staticmethod
    def average_interest(result: SimulationResult) -> float:

        if not result.payments:
            return 0

        return result.final_state.total_interest_paid / len(result.payments)

    @staticmethod
    def average_principal(result: SimulationResult) -> float:

        if not result.payments:
            return 0

        return result.final_state.total_principal_paid / len(result.payments)
