import json
from functools import lru_cache
from pathlib import Path

from fastapi import APIRouter

router = APIRouter()

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "eval_results.json"


@lru_cache(maxsize=1)
def _load_stats() -> dict:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


@router.get("/stats")
async def stats() -> dict:
    return _load_stats()
