from flask import Flask
from api.urna_blueprint import urna_blueprint


app = Flask(__name__)

app.register_blueprint(urna_blueprint)

if __name__ == '__main__':
    app.run(port=5500)
            