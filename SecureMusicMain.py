from flask import Flask, g, request, render_template
import sqlite3

app = Flask(__name__)

DATABASE = 'users.db'


@app.route('/')
@app.route('/index')
def index():
    return 'Test Successful!'


if __name__ == '__main__':
    app.run()

#test