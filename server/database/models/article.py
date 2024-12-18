import uuid

from sqlalchemy import UUID, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from server.database import Base
from server.database.mixins import TimestampMixin

from server.settings import Database


class ArticleModel(Base, TimestampMixin):
    __tablename__ = f'{Database.prefix}article'
    __table_args__ = {
        'extend_existing': True,
        'comment': 'A table with info about the articles',
    }

    id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        default=uuid.uuid4,
        primary_key=True,
        comment='Unique identifier for the article'
    )
    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment='Title of the article'
    )
    text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        comment='Main content of the article'
    )
    source_language: Mapped[str] = mapped_column(
        String,
        nullable=False,
        comment='Source language of the article'
    )
    is_original: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        comment='Flag indicating if the article is an original'
        '(True) or a translation (False)'
    )
    original_article_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(f'{Database.prefix}article.id', ondelete='SET NULL'),
        nullable=True,
        comment='Foreign key to the original article if this'
        'article is a translation'
    )
