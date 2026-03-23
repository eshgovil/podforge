from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Article:
    title: str
    content: str
    source_url: str
    source_name: str
    published_at: datetime | None = None
    id: UUID = field(default_factory=uuid4)
