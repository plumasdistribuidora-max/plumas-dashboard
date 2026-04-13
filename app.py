import os
from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    return Response(content, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
