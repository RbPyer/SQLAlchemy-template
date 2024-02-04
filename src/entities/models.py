from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.entities.enums import Workload, AnnotatedTypes
from src.entities.database import Base


class Workers(Base):
    __tablename__ = "workers"

    id: Mapped[AnnotatedTypes.int_pk]
    username: Mapped[str] = mapped_column(String(256))


class Resumes(Base):
    __tablename__ = "resumes"

    id: Mapped[AnnotatedTypes.int_pk]
    title: Mapped[str]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[AnnotatedTypes.created_at]
    updated_at: Mapped[AnnotatedTypes.updated_at]

