from enum import StrEnum


class EpisodeStatus(StrEnum):
    CREATED = "created"
    ARTICLES_FETCHED = "articles_fetched"
    SUMMARIZED = "summarized"
    SCRIPTED = "scripted"
    SYNTHESIZED = "synthesized"
    DELIVERED = "delivered"
    FAILED = "failed"
