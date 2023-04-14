from datetime import datetime
from pydantic import BaseModel


class Author(BaseModel):
    id: int
    name: str
    username: str
    job: str
    photo: str


class Publication (BaseModel):
    id: int
    title: str
    date: datetime
    author_id: int
    description: str
