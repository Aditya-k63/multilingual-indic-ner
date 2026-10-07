from fastapi import APIRouter

from app.config import settings
from app.schemas import HealthResponse, NerRequest, NerResponse
from app.services.ner_service import extract_entities

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="ok", model=settings.model_repo)


@router.post("/ner", response_model=NerResponse)
async def ner(request: NerRequest) -> NerResponse:
    entities = extract_entities(request.text)
    return NerResponse(
        language=request.language,
        entities=entities,
        entity_count=len(entities),
    )
