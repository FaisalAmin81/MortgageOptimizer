from dataclasses import dataclass


@dataclass
class OptimizationConfig:
    """
    Controls how the optimizer searches for the best mortgage strategy.
    """

    # Settlement limits
    max_settlements: int = 3
    minimum_settlement: float = 500_000

    # Timing rules
    earliest_settlement_month: int = 37
    minimum_months_between: int = 0

    # Strategy
    reduce_emi: bool = True
    final_payoff_with_savings: bool = True

    # Future options
    invest_unused_surplus: bool = False
