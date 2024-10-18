from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory storage for registered users
users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        users.append({'username': username, 'email': email})  # Store user info
        return redirect(url_for('success'))

    return render_template('register.html')

@app.route('/success')
def success():
    return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)
