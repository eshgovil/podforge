from typing import Protocol

from podforge.domain.entities.article import Article


class Summarizer(Protocol):
    def summarize(self, articles: list[Article]) -> str: ...
