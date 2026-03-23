from dataclasses import dataclass, field
from datetime import date
from uuid import UUID, uuid4

from personalized_podcast.domain.entities.article import Article
from personalized_podcast.domain.value_objects.episode_status import EpisodeStatus
from personalized_podcast.domain.value_objects.script_segment import ScriptSegment


@dataclass
class Episode:
    podcast_id: UUID
    date: date
    articles: list[Article] = field(default_factory=list)
    script: list[ScriptSegment] = field(default_factory=list)
    summary: str | None = None
    audio_path: str | None = None
    status: EpisodeStatus = EpisodeStatus.CREATED
    # Provider metadata for traceability
    summarizer_model: str | None = None
    script_model: str | None = None
    speech_provider: str | None = None
    id: UUID = field(default_factory=uuid4)
