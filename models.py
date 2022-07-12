import json
from dataclasses import dataclass


@dataclass
class ReviewData:
    author_name: str
    text: str
    author_url: str = None
    created_at: str = None
    author_photo_url: str = None
    rating: float = None

    def to_json(self):
        return json.dumps(self.__dict__)
