from pathlib import Path
from flask import Flask, request
import logging
import ngrok
import jwt

from utils import *

PORT = 8080
JWT_SECRET = ""
SOLUTION = ""

logging.basicConfig(level=logging.INFO)
listener = ngrok.forward(PORT, authtoken_from_env=True)


app = Flask(__name__)


@app.get("/")
def start():
    global JWT_SECRET
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    JWT_SECRET = str(res_json["jwt_secret"])
    print(f"JWT_SECRET: {JWT_SECRET}")
    print("App URL:", listener.url())
    submit_solution(challenge, solution={"app_url": listener.url()})
    return "Started"


@app.post("/")
def submit():
    global SOLUTION
    try:
        token = jwt.decode(request.get_data(), JWT_SECRET, algorithms=["HS256"])
        if "append" in token:
            SOLUTION += token["append"]
            print(f"SOLUTION: {SOLUTION}")
            return ""
        else:
            return {"solution": SOLUTION}
    except Exception as e:
        logging.error(e)
        return ""


if __name__ == "__main__":
    app.run(port=PORT)
