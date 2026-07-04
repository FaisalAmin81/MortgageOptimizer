from src.models.currency import Currency


def format_money(amount: float, currency: Currency) -> str:
    """
    Format a monetary value using the selected currency.
    """
    return f"{currency.symbol}{amount:,.{currency.decimal_places}f}"