from dataclasses import dataclass


@dataclass(frozen=True)
class ReportField:
    """
    Represents one row in a report.
    """

    label: str

    value: object

    value_type: str
