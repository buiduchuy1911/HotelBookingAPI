from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flasgger import Swagger

from app.config import config_by_name

# Khởi tạo các extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()
ma = Marshmallow()
cors = CORS()
swagger = Swagger()

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    # Swagger template & config
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/"
    }
    
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Hotel Booking API",
            "description": "API documentation for Hotel Booking System",
            "version": "1.0.0"
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header using the Bearer scheme. Example: \"Authorization: Bearer {token}\""
            }
        },
        "security": [
            {
                "Bearer": []
            }
        ]
    }
    swagger.config = swagger_config
    swagger.template = swagger_template
    swagger.init_app(app)
    from app.models import user, hotel, room_type, room, amenity, booking, review

    # Đăng ký Blueprints
    from app.views.auth_routes import auth_bp
    from app.views.hotel_routes import hotel_bp
    from app.views.room_routes import room_bp
    from app.views.amenity_routes import amenity_bp
    from app.views.booking_routes import booking_bp
    from app.views.review_routes import review_bp
    from app.views.admin_routes import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(hotel_bp, url_prefix='/api/hotels')
    app.register_blueprint(room_bp, url_prefix='/api/rooms')
    app.register_blueprint(amenity_bp, url_prefix='/api/amenities')
    app.register_blueprint(booking_bp, url_prefix='/api/bookings')
    app.register_blueprint(review_bp, url_prefix='/api') # /api/hotels/<id>/reviews
    app.register_blueprint(admin_bp, url_prefix='/api/admin')

    # Đăng ký Global Error Handlers
    from app.utils.error_handlers import register_error_handlers
    register_error_handlers(app)

    return app
