import asyncio
from src.controllers.ORM import ORMController
from src.entities.database import Database


async def main():
    db: Database = Database()
    db_controller: ORMController = ORMController()
    await db_controller.create_tables(db)


if __name__ == "__main__":
    asyncio.run(main())
