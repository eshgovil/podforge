from typing import Protocol

from personalized_podcast.domain.entities.article import Article


class Summarizer(Protocol):
    def summarize(self, articles: list[Article]) -> str: ...
