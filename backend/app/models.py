from typing import List, Optional
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field
from pymongo import IndexModel


class URL(Document):
    uuid: UUID = Field(default_factory=uuid4)
    target_url: Optional[str] = None
    url_key: Optional[List] = None

    class Settings:
        indexes = [
            IndexModel("uuid", unique=True),
        ]
