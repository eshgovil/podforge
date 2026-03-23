from typing import Protocol

from podforge.domain.entities.article import Article
from podforge.domain.value_objects.source_config import SourceConfig


class ContentFetcher(Protocol):
    def fetch(self, source: SourceConfig) -> list[Article]: ...
