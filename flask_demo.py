""" A simple flask request handler demo """
#!flask/bin/python
from flask import Flask, request

app = Flask(__name__)


@app.route('/v1/')
def smart():
    """ Example: HTTP GET http://127.0.0.1:5000/v1/?q=hello world """
    query = request.args.get('q')
    return "<html><body><h1>"+str(query)+"</h1></body></html>"

if __name__ == '__main__':
    app.run(debug=True)
