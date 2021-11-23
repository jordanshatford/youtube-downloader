from typing import Optional

from pydantic import BaseModel


class AudioOptions(BaseModel):
    format: str


class Channel(BaseModel):
    name: str
    url: Optional[str]
    thumbnail: Optional[str]


class Video(BaseModel):
    id: str
    url: str
    options: Optional[AudioOptions]
    title: Optional[str]
    duration: Optional[str]
    thumbnail: Optional[str]
    channel: Optional[Channel]


class Session(BaseModel):
    id: str


class Message(BaseModel):
    title: str
    message: str
