# PodForge

An open-source agent that generates personalized daily podcasts from your chosen news sources. Pick your feeds, configure host personalities and voices, and get a multi-host audio podcast delivered wherever you want.

## How It Works

```
RSS Feeds → [Fetch] → Articles → [Summarize] → Briefing → [Script] → Dialog → [Synthesize] → Audio → [Deliver]
```

Each stage is status-gated — if a run fails midway, re-running resumes from where it left off (no duplicate API calls or wasted TTS credits).

## Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (package manager)
- [ffmpeg](https://ffmpeg.org/) (audio processing)

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

### Install

```bash
git clone <repo-url> && cd podforge
uv sync
```

### Configure

1. Copy and edit the example config:

```bash
cp config.example.yaml config.yaml
```

2. Set your API keys:

```bash
export GEMINI_API_KEY="your-key"       # or ANTHROPIC_API_KEY, OPENAI_API_KEY
export ELEVEN_API_KEY="your-key"       # ElevenLabs TTS
```

The LLM provider is configurable via `config.yaml` — any provider supported by [LiteLLM](https://docs.litellm.ai/docs/providers) works out of the box.

### Generate

```bash
uv run podforge generate --config config.yaml
```

Add `-v` for verbose logging, or `--date 2026-03-22` for a specific date.

## Configuration

```yaml
podcast:
  name: "Morning Briefing"
  schedule: "0 7 * * *"           # cron syntax (used by scheduler, Phase 3)
  target_length_minutes: 10       # controls script word count

sources:
  - name: "Hacker News"
    kind: rss
    url: "https://hnrss.org/frontpage"
  - name: "TechCrunch"
    kind: rss
    url: "https://techcrunch.com/feed/"

hosts:
  - name: "Alex"
    personality: "Curious tech enthusiast who asks good follow-up questions"
    voice_id: "pNInz6obpgDQGcFmaJgB"      # ElevenLabs voice ID
    voice_provider: "elevenlabs"
  - name: "Sam"
    personality: "Dry humor, skeptical, always looks for the business angle"
    voice_id: "ErXwobaYiN019PkySvjV"
    voice_provider: "elevenlabs"

providers:
  summarizer:
    provider: gemini                        # any LiteLLM provider
    model: gemini-3-flash-preview
  script_writer:
    provider: gemini
    model: gemini-3-pro-preview
  speech:
    provider: elevenlabs

destinations:
  - kind: file
    path: "./output"
```

### Switching LLM Providers

Any [LiteLLM-supported provider](https://docs.litellm.ai/docs/providers) works — just change the config:

```yaml
# Anthropic
summarizer:
  provider: anthropic
  model: claude-haiku-4-5-20251001

# OpenAI
summarizer:
  provider: openai
  model: gpt-5-mini

# Google Gemini
summarizer:
  provider: gemini
  model: gemini-3-flash-preview

# Local (Ollama)
summarizer:
  provider: ollama
  model: qwen3.5:27b
```

Set the corresponding env var (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GEMINI_API_KEY`) or run locally with Ollama.

## Architecture

```
src/podforge/
├── domain/           # Pure dataclasses, no I/O
├── application/      # Ports (Protocol interfaces) + PipelineService
├── infrastructure/   # Adapters (RSS, LiteLLM, ElevenLabs, pydub, JSON store)
├── cli.py            # Typer CLI
└── main.py           # Composition root
```

- **Domain objects** are `@dataclass` (pure, no I/O)
- **Ports** are `typing.Protocol` classes — any conforming class works as an adapter
- **Config validation** uses Pydantic at the infrastructure boundary
- **Secrets** via environment variables, never in config files
- **Tests** use fakes from `tests/fakes/`, not mocks

## Development

```bash
uv run pytest                          # unit tests
uv run pytest -m integration           # integration tests (requires API keys)
uv run mypy src/                       # type check
uv run ruff check src/ tests/          # lint
uv run ruff format src/ tests/         # format
```

## Responsible Use

This tool generates podcasts for **personal consumption only**, not for commercial use or redistribution. Please respect the original creators:

- **Personal use:** Generated episodes are meant for your own listening. Do not publish, monetize, or commercially distribute them.
- **Paywalled content:** If a source requires a subscription, pay for it. Do not use this tool to circumvent paywalls.
- **Attribution:** If you share episodes beyond personal use, you are responsible for crediting and citing the original sources.
- **Terms of service:** Respect the terms of service of every source you configure. RSS feeds are generally intended for personal consumption.
- **Copyright:** Generated episodes contain AI-summarized versions of original reporting. This is not a substitute for reading the source material — support the journalists and creators whose work makes this possible.

## Cost Estimates

Per 10-minute episode:
- **LLM (summarize + script):** ~$0.01–0.10 depending on provider
- **TTS (ElevenLabs):** ~$1–3 depending on plan
- **Total:** ~$1–3/episode (dominated by TTS)

## License

MIT
