import logging
import shutil
from pathlib import Path

from personalized_podcast.domain.entities.episode import Episode

logger = logging.getLogger(__name__)


class FileChannel:
    def __init__(self, output_dir: str = "./output") -> None:
        self._output_dir = Path(output_dir)
        self._output_dir.mkdir(parents=True, exist_ok=True)

    def deliver(self, episode: Episode, audio_path: str) -> None:
        destination = (
            self._output_dir / f"{episode.date.isoformat()}_{episode.podcast_id}.mp3"
        )
        shutil.copy2(audio_path, destination)
        logger.info("Delivered episode to %s", destination)
