from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(
    app,
    resources={r"/*": {"origins": "*"}}
)

@app.route('/')
def index():
    return 'Frasaria backend API gateway'


# import blueprint here
from rephrase import rephrase

# register blueprint here
app.register_blueprint(rephrase)

if __name__ == '__main__':
    app.run()
