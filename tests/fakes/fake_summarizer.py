from podforge.domain.entities.article import Article


class FakeSummarizer:
    def __init__(self, summary: str = "Fake summary of today's news.") -> None:
        self.summary = summary
        self.called_with: list[Article] | None = None

    def summarize(self, articles: list[Article]) -> str:
        self.called_with = articles
        return self.summary
