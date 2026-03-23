from typing import Protocol

from personalized_podcast.domain.value_objects.host_config import HostConfig
from personalized_podcast.domain.value_objects.script_segment import ScriptSegment


class SpeechSynthesizer(Protocol):
    def synthesize(self, segment: ScriptSegment, host: HostConfig) -> bytes: ...
