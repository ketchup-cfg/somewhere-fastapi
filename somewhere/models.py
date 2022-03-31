from pydantic import BaseModel


class Topic(BaseModel):
    id: int
    name: str
    description: str | None = None
