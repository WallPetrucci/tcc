# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route('/test')
def testing():
    my_json = dict()
    my_json = {
        "status": True
    }
    return jsonify(my_json)


if __name__ == '__main__':
    app.run()
