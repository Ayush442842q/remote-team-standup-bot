import re
from typing import Any

def validate_email(email: str) -> bool:
    """
    Validate an email address.

    Args:
    - email (str): The email address to validate.

    Returns:
    - is_valid (bool): True if the email is valid, otherwise False.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def validate_password(password: str) -> bool:
    """
    Validate a password.

    Args:
    - password (str): The password to validate.

    Returns:
    - is_valid (bool): True if the password is valid, otherwise False.
    """
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True

def validate_input(data: Any) -> bool:
    """
    Validate input data.

    Args:
    - data (Any): The input data to validate.

    Returns:
    - is_valid (bool): True if the input is valid, otherwise False.
    """
    if not isinstance(data, dict):
        return False
    for key, value in data.items():
        if not isinstance(key, str):
            return False
        if value is None:
            return False
    return True