from ti_draft_api.app import app

@app.route("/register")
def register():
  return {"userId": "1234"}