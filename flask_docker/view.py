from flask import Flask
import train
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return train.function_name


if __name__ == "__main__":
    app.run(debug=True)