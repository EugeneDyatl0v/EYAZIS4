import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from server.settings import Database, LOGGER_PREFIX

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

logger = logging.getLogger(LOGGER_PREFIX + __name__)

engine = create_async_engine(Database.url)

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
