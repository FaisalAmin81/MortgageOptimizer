from src.models.currency import Currency


class AppConfig:
    """
    Global application settings.
    """

    DEFAULT_CURRENCY = Currency(
        code="PKR",
        symbol="Rs ",
        decimal_places=2,
    )