from dataclasses import dataclass


@dataclass(frozen=True)
class HostConfig:
    name: str
    personality: str
    voice_id: str
    voice_provider: str = "elevenlabs"
