from dataclasses import dataclass
from typing import Optional


@dataclass
class AnimalBasicInfo:
    id: int
    name: str
    born_at: Optional[int]


@dataclass
class AnimalRawInfo(AnimalBasicInfo):
    friends_with = Optional[str]
