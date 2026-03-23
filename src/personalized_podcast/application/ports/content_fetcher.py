from typing import Protocol

from personalized_podcast.domain.entities.article import Article
from personalized_podcast.domain.value_objects.source_config import SourceConfig


class ContentFetcher(Protocol):
    def fetch(self, source: SourceConfig) -> list[Article]: ...
