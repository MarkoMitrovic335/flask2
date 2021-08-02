import bcrypt

from sqlalchemy import select

from models.base import engine, Base, Session
from models.user import User

# async
async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        # async with Session() as session:
        #     email = 'admin@gmail.com'
        #     superadmin = await session.execute(select(User).where(User.email == email))
        #     superadmin = superadmin.scalar()
        #     if not superadmin:
        #         # Initialize User
        #         password = 'Admin123$'
        #         password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        #         user = User('admin', 'admin', 'admin@gmail.com', password)
                    
        #         # Add user to databese and close session
        #         session.add(user)
        #         await session.flush()
        #         await session.commit()
        #         await session.close()
                
    