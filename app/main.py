from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import meta, ner
from app.services.ner_service import get_ner_pipeline


@asynccontextmanager
async def lifespan(app: FastAPI):
    get_ner_pipeline()
    yield


app = FastAPI(
    title="Indic NER API",
    description="Hindi NER (PER/ORG/LOC) with zero-shot transfer to Bengali, Tamil, Telugu. Model: IndicBERTv2 fine-tuned on Naamapadam.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(ner.router, prefix="/api/v1", tags=["ner"])
app.include_router(meta.router, prefix="/api/v1", tags=["meta"])

STATIC_DIR = Path(__file__).parent / "static"
app.mount("/", StaticFiles(directory=STATIC_DIR, html=True), name="static")
