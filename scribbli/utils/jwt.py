import jwt
from datetime import datetime
from graphql_jwt.settings import jwt_settings


def generate_jwt_payload(user, context=None):
    return {
        'iss': 'scribb.li',
        'sub': str(user.id),
        'exp': int((datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA).timestamp()),
        'iat': int(datetime.utcnow().timestamp()),
        'pseudonym': user.username,
    }
