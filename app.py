#app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, This is my CD Test!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)

