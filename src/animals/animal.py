from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime, timezone

SEC_TO_MILLS = 1000


@dataclass
class AnimalBasicInfo:
    id: int
    name: str = ''
    born_at: Optional[int] = None


@dataclass
class AnimalPage:
    page: int = 0
    total_pages: int = 0
    items: List[AnimalBasicInfo] = field(default_factory=list)

    def __post_init__(self):
        if self.items:
            self.items = [AnimalBasicInfo(**item) for item in self.items]


@dataclass
class AnimalRawInfo(AnimalBasicInfo):
    friends: Optional[str] = None


@dataclass
class AnimalDetails(AnimalRawInfo):

    def __post_init__(self):
        if self.born_at and isinstance(self.born_at, int):
            dt_object = datetime.fromtimestamp(
                self.born_at / SEC_TO_MILLS, tz=timezone.utc
            )
            self.born_at = f'{dt_object.isoformat()[:-9]}Z'

        if isinstance(self.friends, str):
            self.friends = [
                friend.strip() for friend in self.friends.split(',')
            ]
