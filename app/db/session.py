from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from core.config import get_db_url, settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self._engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self._engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def _get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def scoped_session_dependency(self):
        session = self._get_scoped_session()
        yield session
        await session.close()

    async def dispose(self) -> None:
        await self._engine.dispose()


db_helper = DatabaseHelper(
    url=get_db_url(),
    echo=settings.db.echo,
)
