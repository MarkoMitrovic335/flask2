from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# sqlite engine
engine = create_async_engine('sqlite+aiosqlite:///flask_exm.db', echo=True)

# base
Base = declarative_base()

# session
Session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)