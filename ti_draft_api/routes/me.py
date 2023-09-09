from ti_draft_api.app import app
from ti_draft_api.auth import tokens
from ti_draft_api.auth.decorators import require_valid_jwt
from ti_draft_api.auth.jwt_state import JwtState

@app.route("/me")
@require_valid_jwt
def me(jwt_state: JwtState):
  """Allows a user to see who they are logged in as."""
  return {"userId": jwt_state.user_id}