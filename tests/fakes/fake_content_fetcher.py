from podforge.domain.entities.article import Article
from podforge.domain.value_objects.source_config import SourceConfig


class FakeContentFetcher:
    def __init__(self, articles: list[Article] | None = None) -> None:
        self.articles = articles or []

    def fetch(self, source: SourceConfig) -> list[Article]:
        return list(self.articles)
