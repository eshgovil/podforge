import os
from datetime import date

from personalized_podcast.application.ports.speech_synthesizer import (
    SpeechSynthesizer,
)
from personalized_podcast.application.services.pipeline import PipelineService
from personalized_podcast.domain.entities.episode import Episode
from personalized_podcast.domain.value_objects.episode_status import EpisodeStatus
from personalized_podcast.domain.value_objects.source_config import SourceKind
from personalized_podcast.domain.value_objects.speech_provider import SpeechProvider
from personalized_podcast.infrastructure.adapters.elevenlabs_synthesizer import (
    ElevenLabsSynthesizer,
)
from personalized_podcast.infrastructure.adapters.file_channel import FileChannel
from personalized_podcast.infrastructure.adapters.json_episode_store import (
    JsonEpisodeStore,
)
from personalized_podcast.infrastructure.adapters.kokoro_synthesizer import (
    KokoroSynthesizer,
)
from personalized_podcast.infrastructure.adapters.litellm_script_writer import (
    LitellmScriptWriter,
)
from personalized_podcast.infrastructure.adapters.litellm_summarizer import (
    LitellmSummarizer,
)
from personalized_podcast.infrastructure.adapters.pydub_mixer import PydubMixer
from personalized_podcast.infrastructure.adapters.rss_fetcher import RssFetcher
from personalized_podcast.infrastructure.config.loader import load_config


def build_and_run(
    config_path: str,
    target_date: date,
    from_stage: EpisodeStatus | None = None,
) -> Episode:
    podcast, config = load_config(config_path)

    # Build LLM model strings in LiteLLM format: "provider/model"
    summarizer_model = (
        f"{config.providers.summarizer.provider}"
        f"/{config.providers.summarizer.model}"
    )
    script_model = (
        f"{config.providers.script_writer.provider}"
        f"/{config.providers.script_writer.model}"
    )

    # Wire adapters
    fetchers = {SourceKind.RSS: RssFetcher()}
    summarizer = LitellmSummarizer(model=summarizer_model)
    script_writer = LitellmScriptWriter(model=script_model)
    synthesizer: SpeechSynthesizer
    if config.providers.speech.provider == SpeechProvider.KOKORO:
        synthesizer = KokoroSynthesizer()
    else:
        synthesizer = ElevenLabsSynthesizer(
            api_key=os.environ.get("ELEVEN_API_KEY"),
        )
    mixer = PydubMixer()
    episode_store = JsonEpisodeStore()

    channels = [
        FileChannel(output_dir=dest.path or "./output")
        for dest in config.destinations
        if dest.kind == "file"
    ]

    pipeline = PipelineService(
        fetchers=fetchers,
        summarizer=summarizer,
        script_writer=script_writer,
        synthesizer=synthesizer,
        mixer=mixer,
        episode_store=episode_store,
        channels=channels,
        provider_meta={
            "summarizer_model": summarizer_model,
            "script_model": script_model,
            "speech_provider": config.providers.speech.provider.value,
        },
    )

    return pipeline.run(podcast, target_date, from_stage=from_stage)
