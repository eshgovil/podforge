from podforge.domain.value_objects.host_config import HostConfig
from podforge.domain.value_objects.script_segment import (
    ScriptSegment,
    SegmentType,
)


class FakeScriptWriter:
    def __init__(self, segments: list[ScriptSegment] | None = None) -> None:
        self.segments = segments or [
            ScriptSegment(
                host_name="Host", text="Hello!", segment_type=SegmentType.INTRO
            ),
        ]

    def write_script(
        self,
        summary: str,
        hosts: list[HostConfig],
        target_length_minutes: int,
    ) -> list[ScriptSegment]:
        return list(self.segments)
