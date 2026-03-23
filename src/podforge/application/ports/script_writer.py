from typing import Protocol

from podforge.domain.value_objects.host_config import HostConfig
from podforge.domain.value_objects.script_segment import ScriptSegment


class ScriptWriter(Protocol):
    def write_script(
        self,
        summary: str,
        hosts: list[HostConfig],
        target_length_minutes: int,
    ) -> list[ScriptSegment]: ...
