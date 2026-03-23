# PodForge

## Architecture

Layered architecture with clean separation:
- `src/podforge/domain/` — Pure dataclasses, no I/O
- `src/podforge/application/` — Ports (Protocol interfaces) and PipelineService orchestration
- `src/podforge/infrastructure/` — Concrete adapters (RSS, LiteLLM, ElevenLabs, etc.)
- `src/podforge/cli.py` — Typer CLI entrypoint
- `src/podforge/main.py` — Composition root (wires adapters)

## Pipeline

Linear, status-gated: Fetch → Summarize → Script → Synthesize → Mix → Deliver.
Each stage persists progress via `EpisodeStatus` for idempotent re-runs.

## Commands

- `uv run pytest` — run unit tests
- `uv run pytest -m integration` — run integration tests (requires API keys)
- `uv run mypy src/` — type check
- `uv run ruff check src/ tests/` — lint
- `uv run ruff format src/ tests/` — format
- `uv run podcast generate --config config.yaml` — generate an episode

## Conventions

- Domain objects are `@dataclass` (pure, no I/O)
- Config validation uses Pydantic (infrastructure boundary only)
- Ports are `typing.Protocol` classes in `application/ports/`
- LLM calls go through LiteLLM (provider-agnostic)
- Secrets via environment variables, never in config files
- Tests use fakes from `tests/fakes/`, not mocks
