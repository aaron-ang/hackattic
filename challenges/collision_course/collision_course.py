import sys
from pathlib import Path
import subprocess
import base64

FILE_DIR = Path(__file__).parent
sys.path.append(FILE_DIR.parent.as_posix())

from utils import *

HASHCLASH_PATH = FILE_DIR / "hashclash"
FASTCOLL_PATH = HASHCLASH_PATH / "bin" / "md5_fastcoll"


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    prefix = str(res_json["include"])
    print(f"prefix: {prefix}")

    with open(FILE_DIR / "input", "w") as f:
        f.write(prefix)

    if not HASHCLASH_PATH.exists():
        subprocess.run(["git", "submodule", "update", "--init", "--recursive"])

    if not FASTCOLL_PATH.exists():
        # If this fails, go to build.sh
        #   set : ${BOOST_VERSION:=<your local boost version>}
        #   set : ${BOOST_INSTALL_PREFIX:=<your boost path, e.g. /opt/homebrew/Cellar/boost/$BOOST_VERSION>}
        subprocess.run([f"cd {HASHCLASH_PATH} && ./build.sh"], shell=True, check=True)

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
