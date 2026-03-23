from typing import Protocol

from podforge.domain.value_objects.host_config import HostConfig
from podforge.domain.value_objects.script_segment import ScriptSegment


class SpeechSynthesizer(Protocol):
    def synthesize(self, segment: ScriptSegment, host: HostConfig) -> bytes: ...
