from dataclasses import dataclass
from enum import StrEnum


class SourceKind(StrEnum):
    RSS = "rss"
    WEB_PAGE = "web_page"
    API = "api"


@dataclass(frozen=True)
class SourceConfig:
    name: str
    kind: SourceKind
    url: str
    auth: str | None = None
