from flask import Flask
from config import Config
from models import db
from routes import routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Escuchar en todas las interfaces para que el hosting pueda acceder
    app.run(host="0.0.0.0", port=5000)
