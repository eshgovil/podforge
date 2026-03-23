from podforge.domain.entities.episode import Episode


class FakeDeliveryChannel:
    def __init__(self) -> None:
        self.delivered: list[tuple[Episode, str]] = []

    def deliver(self, episode: Episode, audio_path: str) -> None:
        self.delivered.append((episode, audio_path))
