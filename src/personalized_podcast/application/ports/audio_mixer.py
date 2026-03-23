from typing import Protocol


class AudioMixer(Protocol):
    def mix(self, audio_segments: list[bytes], output_path: str) -> str: ...
