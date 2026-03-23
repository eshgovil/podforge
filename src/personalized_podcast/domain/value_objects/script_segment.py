from dataclasses import dataclass
from enum import StrEnum


class SegmentType(StrEnum):
    INTRO = "intro"
    DISCUSSION = "discussion"
    TRANSITION = "transition"
    OUTRO = "outro"


@dataclass(frozen=True)
class ScriptSegment:
    host_name: str
    text: str
    segment_type: SegmentType = SegmentType.DISCUSSION
