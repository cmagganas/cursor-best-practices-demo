from pydantic import (
    Field,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class Settings(BaseSettings):
    """Settings for the files API.

    Pydantic BaseSettings docs: https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage
    FastAPI guide to managing settings: https://fastapi.tiangolo.com/advanced/settings/
    """

    api_key: str = Field(alias='my_api_key')  

    model_config = SettingsConfigDict(case_sensitive=False)