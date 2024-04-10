from pathlib import Path
import requests
from tempfile import NamedTemporaryFile, TemporaryDirectory
import subprocess
from zipfile import ZipFile

from utils import *

SECRET_FILE = "secret.txt"


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    r = requests.get(res_json["zip_url"])

    with NamedTemporaryFile() as f:
        f.write(r.content)
        print(f.name)
        ps = subprocess.run(
            ["fcrackzip", "-b", "-c", "a1", "-l", "4-6", "-u", f.name],
            stdout=subprocess.PIPE,
        )
        output = ps.stdout.decode().strip()
        print(output)
        sub = "pw == "
        password = output[output.find(sub) + len(sub) :]
        print(password)

        with TemporaryDirectory() as tmpdir:
            with ZipFile(f.name) as z:
                z.extract(member=SECRET_FILE, path=tmpdir, pwd=password.encode())
            with open(Path(tmpdir) / SECRET_FILE) as f:
                secret = f.read().strip()
                print(secret)
                res = submit_solution(challenge, {"secret": secret})
                print(res)


if __name__ == "__main__":
    main()
