import jwt

from ti_draft_api.auth.jwt_state import JwtState

JWT_ALGO = "HS256"

def get_jwt_secret() -> str:
  # TODO: Find a way to set this properly
  return "dev_secret_key_1234"

def generate_auth_token(user_id: str) -> str:
  return jwt.encode({"user_id": user_id, "ver": 1}, get_jwt_secret(), algorithm=JWT_ALGO)

def validate_auth_token(token: str) -> JwtState:
  payload = jwt.decode(token, get_jwt_secret(), algorithms=JWT_ALGO)
  return JwtState(payload["user_id"])