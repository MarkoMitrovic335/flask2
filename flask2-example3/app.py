from flask import Flask
from models.user import User
from models.base import Session
from common.initialize_models import init_models
from flask import Blueprint, request, jsonify
from sqlalchemy import select
import asyncio

app = Flask('__name__')

user = Blueprint('user', __name__, url_prefix='/user')


@app.get('/')
async def my_get_endpoint():
    return 'Server is running...'


@app.post('/post')
async def my_post_endpoint():
    return 'Post method called - working...'


@user.post('/create')
async def create():
    
    data = request.get_json()
    
    if not data:
        raise Exception('User data is not valid')
    
    user_dict = data.get('user')
       
    user = User(**user_dict)
    
    async with Session() as session:
        session.add(user)
        await session.commit()
        await session.close()    
    
    response_dict = {
        'user':{
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'password': user.password
        }
    }
    
    return jsonify(response_dict)


@user.get('/all')
async def get_all_user():
    users = []
    async with Session() as session:
        result = await session.execute(select(User))
        result_ = result.scalars()   
        for user in result_:
            response_dict = {
                'user':{
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'password': user.password
                }
            }
            
            users.append(response_dict)
    
    return jsonify({
        'data': users
    })


app.register_blueprint(user)


if __name__ == '__main__':
    
    asyncio.run(init_models())
    
    app.run(host='localhost', port=8080, debug=True)