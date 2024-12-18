import datetime

from sqlalchemy.orm import Mapped, mapped_column


class TimestampMixin:
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now(datetime.UTC).replace(tzinfo=None),
        comment='Timestamp when the record was created'
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.now(datetime.UTC).replace(tzinfo=None),
        comment='Timestamp when the record was last updated'
    )
