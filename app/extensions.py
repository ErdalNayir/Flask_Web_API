from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail

# SQLAlchemy nesnesini oluşturun
db = SQLAlchemy()

# Veritabanı migrasyon işlevlerini sağlayan nesneyi oluşturun
migrate = Migrate()

# JWT işlevlerini sağlayan nesneyi oluşturun
jwt = JWTManager()

# E-posta gönderme işlemleri için nesneyi oluşturun
mail = Mail()
