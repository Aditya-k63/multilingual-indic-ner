from functools import lru_cache

from transformers import pipeline

from app.config import settings
from app.schemas import Entity


@lru_cache(maxsize=1)
def get_ner_pipeline():
    return pipeline(
        "token-classification",
        model=settings.model_repo,
        aggregation_strategy="simple",
    )


def extract_entities(text: str) -> list[Entity]:
    ner = get_ner_pipeline()
    raw = ner(text)
    return [
        Entity(
            text=item["word"],
            type=item["entity_group"],
            score=round(float(item["score"]), 4),
            start=int(item["start"]),
            end=int(item["end"]),
        )
        for item in raw
    ]
