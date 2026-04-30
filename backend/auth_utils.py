import jwt
from datetime import datetime, timedelta

def create_jwt_token(user_id: int, secret_key: str) -> str:
    """
    Create a JWT token for a given user ID.

    Args:
    - user_id (int): The ID of the user.
    - secret_key (str): The secret key for JWT encryption.

    Returns:
    - token (str): The generated JWT token.
    """
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token

def verify_jwt_token(token: str, secret_key: str) -> int:
    """
    Verify a JWT token and return the user ID if valid.

    Args:
    - token (str): The JWT token to verify.
    - secret_key (str): The secret key for JWT decryption.

    Returns:
    - user_id (int): The user ID if the token is valid, otherwise None.
    """
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None