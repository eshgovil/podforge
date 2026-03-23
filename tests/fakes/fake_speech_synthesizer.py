from podforge.domain.value_objects.host_config import HostConfig
from podforge.domain.value_objects.script_segment import ScriptSegment


class FakeSpeechSynthesizer:
    def __init__(self) -> None:
        self.calls: list[tuple[ScriptSegment, HostConfig]] = []

    def synthesize(self, segment: ScriptSegment, host: HostConfig) -> bytes:
        self.calls.append((segment, host))
        return b"fake audio data"
