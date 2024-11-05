import jwt
import datetime
from os import getenv


def token_checker():
    pass

def generate_token(id):
    key = getenv("SECRET_KEY")
    payload = {
        "user_id": id,
        "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, key, algorithm='HS256')

    return token