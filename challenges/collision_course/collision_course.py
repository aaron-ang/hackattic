import sys
from pathlib import Path
import subprocess
import base64

FILE_DIR = Path(__file__).parent

sys.path.append(FILE_DIR.parent.as_posix())
print(sys.path)

from utils import *

FASTCOLL_PATH = FILE_DIR / "hashclash" / "bin" / "md5_fastcoll"


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    prefix = str(res_json["include"])
    print(f"prefix: {prefix}")

    with open(FILE_DIR / "input", "w") as f:
        f.write(prefix)

    subprocess.run(
        [
            FASTCOLL_PATH.as_posix(),
            "-p",
            (FILE_DIR / "input").as_posix(),
            "-o",
            (FILE_DIR / "msg1.bin").as_posix(),
            (FILE_DIR / "msg2.bin").as_posix(),
        ]
    )

    files = []
    with open(FILE_DIR / "msg1.bin", "rb") as f:
        files.append(base64.b64encode(f.read()).decode())
    with open(FILE_DIR / "msg2.bin", "rb") as f:
        files.append(base64.b64encode(f.read()).decode())
    print(files)

    res = submit_solution(challenge, {"files": files})
    print(res)


if __name__ == "__main__":
    main()
