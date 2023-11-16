from flask import Flask
from ..extensions import db


# SQLAlchemy nesnesini oluşturun


def init_app(app):
    # Veritabanı bağlantı bilgilerini yapılandırma dosyasından alın
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://erdal:[PasswordHere]@localhost/yakuperdal'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Flask uygulamasını veritabanına bağlayın
    db.init_app(app)

