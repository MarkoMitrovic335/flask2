import toml

from flask import Flask

app = Flask('__name__')

@app.route('/home', methods=['GET'])
def my_get_endpoint():
    return 'This is home page...'


app.config.from_file('config.toml', toml.load)