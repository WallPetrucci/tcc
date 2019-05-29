# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print("Path: {}".format(path))
    return render_template("vue/index.html")


@app.route('/api/v1/foo')
def api_foo():
    return jsonify("API V1 FOO"), 200


if __name__ == '__main__':
    app.run()
