from ti_draft_api.auth import tokens
from flask import request

def require_valid_jwt(f):
  def decorator():
    try:
      jwt_state = tokens.validate_auth_token(request.authorization.token)
    except Exception:
      return {"errorCode": "INVALID_JWT"}, 401
    return f(jwt_state)
  return decorator