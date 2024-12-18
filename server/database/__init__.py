import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from settings import Database, LOGGER_PREFIX

from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase

logger = logging.getLogger(LOGGER_PREFIX + __name__)

engine = create_async_engine(
    Database.url,
    pool_size=Database.pool_size,
    max_overflow=Database.max_overflow,
    pool_recycle=Database.pool_recycle,
    pool_pre_ping=Database.pool_pre_ping
)

Session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    pass


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        try:
            yield session
        except Exception as e:
            logger.warning('Session rollback because of exception: %s', e)
            await session.rollback()
            raise e
        finally:
            await session.close()