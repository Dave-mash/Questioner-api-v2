from flask import Flask
from app.db_config import create_tables, conn
from instance.config import app_config

def create_app(config_name="development"):
    app = Flask(__name__)
    create_tables()
    cur = conn.cursor()

    return app
