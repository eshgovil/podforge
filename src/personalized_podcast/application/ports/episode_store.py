from datetime import date
from typing import Protocol
from uuid import UUID

from personalized_podcast.domain.entities.episode import Episode


class EpisodeStore(Protocol):
    def save(self, episode: Episode) -> None: ...

    def load(self, podcast_id: UUID, target_date: date) -> Episode | None: ...
