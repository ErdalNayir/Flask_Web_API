from datetime import timedelta


class Config:
    DEBUG = True
    SECRET_KEY = 'RxPmeFGmr6dEld19HY7J8Cu4WZi7QbVF'

    # Veritabanı bağlantı ayarları
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://erdal:*2001*2001*@localhost/yakuperdal'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT yapılandırması
    JWT_SECRET_KEY = 'BzaNDVnDnRJgvzY1oafYRINBG5KP5wTU'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    # E-posta yapılandırması
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'erdal.nayir2001@gmail.com'
    MAIL_PASSWORD = '*2001*2001*'