from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import registry, Mapped, mapped_column

mapper_registry = registry()


@mapper_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(init= False, primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    voice: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(init=False, server_default=func.now())