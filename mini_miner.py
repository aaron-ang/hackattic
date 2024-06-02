from pathlib import Path
import json
from hashlib import sha256

from utils import *


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    difficulty = int(res_json["difficulty"])
    block = dict(sorted(res_json["block"].items()))

    i = 0
    while True:
        block["nonce"] = i
        block_str = json.dumps(block).replace(" ", "")
        hash = sha256(block_str.encode()).hexdigest()
        if not verify_difficulty(hash, difficulty):
            i += 1
        else:
            print(f"Found nonce: {i}")
            submit_solution(challenge, solution={"nonce": i})
            return


def verify_difficulty(hash: str, difficulty: int):
    """verify that the first DIFFICULTY bits of the hash are 0"""
    hash_int = int(hash, base=16)
    for i in range(difficulty):
        if hash_int & (1 << (256 - i - 1)):
            return False
    return True


if __name__ == "__main__":
    main()
