from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_repo: str = "neuronsbyisshu/indicbert-hi-ner-naamapadam"
    supported_languages: tuple[str, ...] = ("hi", "bn", "ta", "te")
    max_text_length: int = 5000


settings = Settings()
