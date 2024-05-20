from rest_framework.exceptions import APIException

class NoAuthException(APIException):
    """Exception when user is Anonymus or not token was passed."""
    status_code = 401
    default_detail = 'No autorized'
    default_code = 'no_auth_permission'