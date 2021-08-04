from sqlalchemy import select
from .base import engine, Base, Session

# async
async def initialize_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)