import toml

from flask import Flask


app = Flask('__name__')


# @app.route('/', methods=['GET'])
# def server_running():
#     return 'Server running. . .'


# @app.route('/home', methods=['GET'])
# def home_page():
#     return 'This is home page. . .'


@app.get('/first')
def my_get_endpoint():
    return 'This was a GET request.'


@app.post('/second')
def my_post_endpoint():
    return 'This was a POST request.'


if __name__ == '__main__':
    app.run(host='localhost', port=1989, debug=True)

# app.config.from_file('config.toml', toml.load)