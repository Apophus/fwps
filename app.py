#!usr/bin/python
from dlask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='color:red'> Hello Flask</h1>"


if __name__ == '__main__':
    app.run()
