from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker
from src.controllers.settings import SettingsController
from src.entities.database import Database, Base
from src.entities.models import Workers, Resumes


class ORMController:

    @staticmethod
    async def create_tables(db: Database):
        async with db.async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def select_from_workers(db: Database, worker_id: int | None = None):
        pass

    @staticmethod
    async def update_worker(db: Database, worker_id: int):
        pass

    @staticmethod
    async def insert_worker(db: Database, worker_id: int):
        pass

    @staticmethod
    async def delete_worker(db: Database):
        async with db.async_session_factory() as session:
            await session.commit()
