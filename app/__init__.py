from flask import Flask
from .api.v2.views.user_views import v2 as user_v2    
from .api.v2.views.meetup_views import v2 as meetup_v2    
from .api.v2.views.question_views import v2 as question_v2    
from config import app_config

def create_app(config_name="development"):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config["development"])
    app.register_blueprint(user_v2)
    app.register_blueprint(meetup_v2)
    app.register_blueprint(question_v2)

    return app
