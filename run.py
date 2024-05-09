from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app= Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return "inicio"



if __name__ == '__main__':
    app.run(debug = True)
