from flask import Flask

app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
  return {
    "status": "ok"
  }

def _import_routes():
  import ti_draft_api.routes.login
  import ti_draft_api.routes.register
  import ti_draft_api.routes.me

_import_routes()