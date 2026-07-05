from dataclasses import dataclass


@dataclass(frozen=True)
class ValueType:

    CURRENCY = "currency"

    PERCENT = "percent"

    INTEGER = "integer"

    TEXT = "text"

    DATE = "date"
