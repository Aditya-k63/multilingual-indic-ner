from typing import Literal

from pydantic import BaseModel, Field

LanguageCode = Literal["hi", "bn", "ta", "te"]


class NerRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000)
    language: LanguageCode | None = None


class Entity(BaseModel):
    text: str
    type: str
    score: float
    start: int
    end: int


class NerResponse(BaseModel):
    language: LanguageCode | None
    entities: list[Entity]
    entity_count: int


class HealthResponse(BaseModel):
    status: str
    model: str
