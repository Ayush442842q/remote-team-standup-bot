from typing import Dict

def format_success_response(data: Dict) -> Dict:
    """
    Format a successful response.

    Args:
    - data (Dict): The data to include in the response.

    Returns:
    - response (Dict): The formatted response.
    """
    return {"success": True, "data": data}

def format_error_response(error_code: int, error_message: str) -> Dict:
    """
    Format an error response.

    Args:
    - error_code (int): The error code.
    - error_message (str): The error message.

    Returns:
    - response (Dict): The formatted response.
    """
    return {"error": {"code": error_code, "message": error_message}}

def get_request_data(request: Dict) -> Dict:
    """
    Get the data from a request.

    Args:
    - request (Dict): The request data.

    Returns:
    - data (Dict): The extracted data.
    """
    return request.get("data", {})