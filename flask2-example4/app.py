import asyncio
from flask import Flask

from routes.user_routes import user_bp
from config.initialize import initialize_models

# initialize Flask app
app = Flask('__name__')


@app.get('/')
async def my_get_endpoint():
    return 'Server is running...'


# regiter blueprints
app.register_blueprint(user_bp)


if __name__ == '__main__':
    
    asyncio.run(initialize_models())
    
    app.run(host='localhost', port=8080, debug=True)