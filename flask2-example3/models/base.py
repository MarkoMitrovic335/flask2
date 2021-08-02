
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

# sqlite
engine = create_async_engine('sqlite+aiosqlite:///flask_example.db', echo=True)

# async session
Base = declarative_base()
Session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)