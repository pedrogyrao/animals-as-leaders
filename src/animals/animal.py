from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class AnimalBasicInfo:
    id: int
    name: str = ''
    born_at: Optional[int] = None


@dataclass
class AnimalRawInfo(AnimalBasicInfo):
    friends_with = Optional[str]


@dataclass
class AnimalPage:
    page: int = 0
    total_pages: int = 0
    items: List[AnimalBasicInfo] = field(default_factory=list)
