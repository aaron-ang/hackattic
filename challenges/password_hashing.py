from pathlib import Path
import base64
import hmac
from hashlib import sha256, pbkdf2_hmac
import scrypt

from utils import *


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    password = str(res_json["password"])
    sha256_hash = sha256(password.encode()).hexdigest()

    salt = str(res_json["salt"])
    salt_bytes = base64.b64decode(salt)
    hmac_hash = hmac.new(salt_bytes, password.encode(), sha256).hexdigest()

    pbkdf2_cfg = res_json["pbkdf2"]
    pbkdf2_hash = pbkdf2_hmac(
        hash_name=pbkdf2_cfg["hash"],
        password=password.encode(),
        salt=salt_bytes,
        iterations=pbkdf2_cfg["rounds"],
    ).hex()

    scypt_cfg = res_json["scrypt"]
    scrypt_hash = scrypt.hash(
        password,
        salt=salt_bytes,
        N=scypt_cfg["N"],
        r=scypt_cfg["r"],
        p=scypt_cfg["p"],
        buflen=scypt_cfg["buflen"],
    ).hex()

    solution = {
        "sha256": sha256_hash,
        "hmac": hmac_hash,
        "pbkdf2": pbkdf2_hash,
        "scrypt": scrypt_hash,
    }
    res = submit_solution(challenge, solution)
    print(res)


if __name__ == "__main__":
    main()
