import toml

from flask import Flask

app = Flask('__name__')

@app.route('/', methods=['GET'])
def server_running():
    return 'Server running. . .'

@app.route('/home', methods=['GET'])
def home_page():
    return 'This is home page. . .'


app.config.from_file('config.toml', toml.load)