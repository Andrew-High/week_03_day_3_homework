from flast import Flask

app = Flask(__name__)
from controllers import controllers

if __name__ == "__main__":
    app.run(debug=True)