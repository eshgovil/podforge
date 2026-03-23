import logging

from elevenlabs import ElevenLabs

from podforge.domain.value_objects.host_config import HostConfig
from podforge.domain.value_objects.script_segment import ScriptSegment

logger = logging.getLogger(__name__)


class ElevenLabsSynthesizer:
    def __init__(self, api_key: str | None = None) -> None:
        self._client = ElevenLabs(api_key=api_key)

    def synthesize(self, segment: ScriptSegment, host: HostConfig) -> bytes:
        logger.debug(
            "Synthesizing segment for %s (%d chars)",
            host.name,
            len(segment.text),
        )
        audio_iterator = self._client.text_to_speech.convert(
            voice_id=host.voice_id,
            text=segment.text,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )
        return b"".join(audio_iterator)
