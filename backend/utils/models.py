from typing import Optional

from pydantic import BaseModel


class Channel(BaseModel):
    name: str
    url: Optional[str]
    thumbnail: Optional[str]


class Video(BaseModel):
    id: str
    url: str
    title: Optional[str]
    duration: Optional[str]
    thumbnail: Optional[str]
    channel: Optional[Channel]


class Message(BaseModel):
    title: str
    message: str
