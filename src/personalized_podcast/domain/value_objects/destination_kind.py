from enum import StrEnum


class DestinationKind(StrEnum):
    FILE = "file"
    SLACK = "slack"
    EMAIL = "email"
