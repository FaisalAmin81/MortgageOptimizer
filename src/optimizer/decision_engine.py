class DecisionEngine:
    """
    Decides whether a settlement should occur.
    """

    @staticmethod
    def should_settle(context) -> bool:
        raise NotImplementedError
