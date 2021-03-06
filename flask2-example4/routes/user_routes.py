from flask import Blueprint, request, jsonify
from sqlalchemy import select

from models.user import User
from config.base import Session


user_bp = Blueprint('user', __name__, url_prefix='/user')


# post/create
@user_bp.post('/create')
async def create():
    
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Missing data!'}), 400
    
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


# login
@user_bp.post('/login')
async def login():
    
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    async with Session() as session:
        try: 
            # Get user by id
            user = await session.execute(select(User).where(User.email == email))
            user = user.scalar()
            
            if not user.password == password:
                return jsonify({'error': 'Wrong credentials!'}), 400
            
            response_dict = {
                'user':{
                    'id': user._id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'password': user.password
                }
            } 

            await session.flush()
            await session.commit()
            await session.close()
        except:
            return jsonify({'error': 'User not found! - Wrong email address'}), 404
    
    return jsonify(response_dict)


# get all
@user_bp.post('/all')
async def get_all():
    users = []
    async with Session() as session:
        result = await session.execute(select(User))
        result_ = result.scalars()   
        for user in result_:
            response_dict = {
                'user':{
                    'id': user._id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'password': user.password
                }
            }
            
            users.append(response_dict)
    
    return jsonify({'data': users})


# get
@user_bp.get('/get')
async def get():
    
    args = request.args
    id = args.get('id')
    
    if not id:
        return jsonify({'error': 'User id is required'}), 400 
    
    async with Session() as session:
        try: 
            # Get user by id
            user = await session.execute(select(User).where(User._id == id))
            user = user.scalar()
            
            response_dict = {
                'user':{
                    'id': user._id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'password': user.password
                }
            } 

            await session.flush()
            await session.commit()
            await session.close()
        except:
            return jsonify({'error': 'User not found!'}), 404

    return jsonify({'data': response_dict}), 200


# remove/delete
@user_bp.post('/remove')
async def remove_user():
    
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Data is required'}), 400 

    id = data.get('id')
    
    if not id:
        return jsonify({'error': 'User id is required'}), 400 

    async with Session() as session:
        try: 
            # Get user by id
            user = await session.execute(select(User).where(User._id == id))
            user = user.scalar() 

            await session.delete(user)
            await session.commit()
            await session.close()
        except:
            return jsonify({'error': 'User not found!'}), 404

    return jsonify({
        'data': 'User deleted!'
    })
    

# update
@user_bp.post('/update')
async def update():
    
    args = request.args
    id = args.get('id')
    
    if not id:
        return jsonify({'error': 'User id is required'}), 400 
    
    async with Session() as session:
        
        # Get user by id
        user = await session.execute(select(User).where(User._id == id))
        user = user.scalar() 

        if not user:
            return jsonify({
                'error': f'User with id: {id} not found'
            }), 404
            
        data = request.get_json()    
            
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        new_email = data.get('email')
        
        if new_email:
            check_user = await session.execute(select(User).where(User.email == new_email))
            check_user = check_user.scalar()

            if check_user:
                return jsonify({
                    'error': 'Email already exists, change email and try again'
                }), 400
            else:
                user.email = new_email
    
        session.add(user)
        await session.commit()
        await session.close()
        
        response_dict = {
                'user':{
                    'id': user._id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'password': user.password
                }
            } 

    return jsonify({'data': response_dict}), 200