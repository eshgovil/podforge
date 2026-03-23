import io
import logging

from pydub import AudioSegment  # type: ignore[import-untyped]

logger = logging.getLogger(__name__)


class PydubMixer:
    def mix(self, audio_segments: list[bytes], output_path: str) -> str:
        if not audio_segments:
            raise ValueError("No audio segments to mix")

        logger.info("Mixing %d audio segments", len(audio_segments))
        combined = AudioSegment.empty()
        for segment_bytes in audio_segments:
            segment = AudioSegment.from_mp3(io.BytesIO(segment_bytes))
            combined += segment

        combined.export(output_path, format="mp3")
        logger.info("Mixed audio exported to %s", output_path)
        return output_path
