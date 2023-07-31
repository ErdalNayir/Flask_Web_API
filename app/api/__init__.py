from ..Domain.user import User
import hashlib


def verify_user(username, password):
    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    user = User.query.filter_by(username=username, password=hashed_pass).first()
    return user
