from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "my name is Faith"

if __name__ == "__main__":
    app.run(debug=True)