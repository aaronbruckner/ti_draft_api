import jwt
from datetime import datetime, timezone, timedelta

from ti_draft_api.auth.jwt_state import JwtState

JWT_ALGO = "HS256"
SECS_IN_ONE_DAY = 86_400

def get_jwt_secret() -> str:
  # TODO: Find a way to set this properly
  return "dev_secret_key_1234"

def generate_auth_token(user_id: str, ttl_secs=SECS_IN_ONE_DAY) -> str:
  """Generates a JWT for a single user with a known expiration time."""
  exp_time = datetime.now(tz=timezone.utc) + timedelta(seconds=ttl_secs)
  return jwt.encode({"user_id": user_id, "ver": 1, "exp": exp_time}, get_jwt_secret(), algorithm=JWT_ALGO)

def validate_auth_token(token: str) -> JwtState:
  """Extracts important details from the JWT, raising an exception should it be inlvaid."""
  payload = jwt.decode(token, get_jwt_secret(), algorithms=JWT_ALGO)
  return JwtState(payload["user_id"])