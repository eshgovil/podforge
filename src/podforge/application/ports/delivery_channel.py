from typing import Protocol

from podforge.domain.entities.episode import Episode


class DeliveryChannel(Protocol):
    def deliver(self, episode: Episode, audio_path: str) -> None: ...
