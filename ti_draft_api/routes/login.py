from ti_draft_api.app import app
from ti_draft_api.auth import tokens

@app.route("/login")
def login():
  return {"access_token": tokens.generate_auth_token("1234")}