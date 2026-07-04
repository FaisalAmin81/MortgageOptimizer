from dataclasses import dataclass


@dataclass
class SettlementRule:
    """
    Rules governing mortgage settlements.
    """

    minimum_amount: float = 500_000

    reduce_emi: bool = True

    keep_original_term: bool = True