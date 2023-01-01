from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from lupa import LuaRuntime
from lupa._lupa import LuaError

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)

lua = LuaRuntime()
sandbox = lua.require("sandbox")[0]


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/code")
@limiter.limit("3/second", override_defaults=False)
def code():
    try:
        finished, response = sandbox.run(request.json["code"])
        return {"code": response}
    except LuaError:
        return {"code": "Script canceled because it uses too much resources."}


app.run(debug=True)
