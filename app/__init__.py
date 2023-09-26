from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Flask-Migrate
from config import config


db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate = Migrate(app, db)  # Initialize Flask-Migrate
    
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app
