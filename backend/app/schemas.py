from typing import List, Optional

from pydantic import BaseModel, SecretStr


class CreateShortURL(BaseModel):
    target_url: str
    url_key: Optional[str]


class BaseURL(BaseModel):
    target_url: SecretStr


class ShortURL(BaseURL):
    url_key: Optional[List] = None

    class Config:
        orm_mode = True
