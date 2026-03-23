from datetime import date
from uuid import UUID

from podforge.domain.entities.episode import Episode


class FakeEpisodeStore:
    def __init__(self) -> None:
        self.episodes: dict[str, Episode] = {}

    def save(self, episode: Episode) -> None:
        key = f"{episode.podcast_id}_{episode.date.isoformat()}"
        self.episodes[key] = episode

    def load(self, podcast_id: UUID, target_date: date) -> Episode | None:
        key = f"{podcast_id}_{target_date.isoformat()}"
        return self.episodes.get(key)
