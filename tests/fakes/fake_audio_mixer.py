class FakeAudioMixer:
    def __init__(self) -> None:
        self.called_with: list[bytes] | None = None

    def mix(self, audio_segments: list[bytes], output_path: str) -> str:
        self.called_with = audio_segments
        return output_path
