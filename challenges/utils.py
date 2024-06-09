import os
import requests

from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")


def get_challenge(name: str) -> dict:
    r = requests.get(
        f"https://hackattic.com/challenges/{name}/problem?access_token={ACCESS_TOKEN}"
    )
    r.raise_for_status()
    return r.json()


def submit_solution(name: str, solution: dict) -> dict:
    r = requests.post(
        f"https://hackattic.com/challenges/{name}/solve?access_token={ACCESS_TOKEN}&playground=1",
        json=solution,
    )
    r.raise_for_status()
    return r.json()
