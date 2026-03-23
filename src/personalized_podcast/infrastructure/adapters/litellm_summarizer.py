import logging

import litellm

from personalized_podcast.domain.entities.article import Article

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a news editor preparing a briefing for a podcast. "
    "Summarize the following articles into a concise briefing. "
    "Group related stories together. "
    "Highlight what is most interesting, surprising, or consequential. "
    "Keep it factual but engaging. Write in a way that gives podcast hosts "
    "enough material to have a natural conversation."
)


class LitellmSummarizer:
    def __init__(self, model: str = "anthropic/claude-haiku-4-5-20251001") -> None:
        self._model = model

    def summarize(self, articles: list[Article]) -> str:
        articles_text = "\n\n---\n\n".join(
            f"**{a.title}** ({a.source_name})\n{a.content}" for a in articles
        )
        logger.info("Summarizing %d articles with %s", len(articles), self._model)

        response = litellm.completion(
            model=self._model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": (
                        "Summarize these articles for today's podcast:\n\n"
                        + articles_text
                    ),
                },
            ],
        )

        content: str | None = response.choices[0].message.content
        if not content:
            raise RuntimeError("Summarizer returned empty response")
        return content
