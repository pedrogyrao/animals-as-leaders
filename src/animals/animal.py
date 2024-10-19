from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime, timezone


SEC_TO_MILLIS = 1000


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


@dataclass
class AnimalRawInfo(AnimalBasicInfo):
    friends: Optional[str] = None


@dataclass
class AnimalDetails(AnimalRawInfo):

    def __post_init__(self):
        if self.born_at:
            dt_object = datetime.fromtimestamp(
                self.born_at / SEC_TO_MILLIS, tz=timezone.utc
            )
            self.born_at = dt_object.isoformat().replace('+00:00', 'Z')

        if self.friends:
            self.friends = [
                friend.strip() for friend in self.friends.split(',')
            ]
