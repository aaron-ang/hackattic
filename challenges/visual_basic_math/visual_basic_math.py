import sys
from pathlib import Path
from PIL import Image
from io import BytesIO
import subprocess
import pytesseract
import shutil

FILE_DIR = Path(__file__).parent
sys.path.append(FILE_DIR.parent.as_posix())

from utils import *


def main():
    while True:
        challenge = Path(__file__).stem
        res_json = get_challenge(challenge)
        image_url = res_json["image_url"]

        tess_dir = FILE_DIR / "tessdata_best"
        if not tess_dir.exists():
            subprocess.run(
                [
                    "git",
                    "clone",
                    "https://github.com/tesseract-ocr/tessdata_best",
                    f"{FILE_DIR}/tessdata_best",
                ]
            )

        b = requests.get(image_url).content
        image = Image.open(BytesIO(b)).convert("L")
        # image.show()

        config = f"--psm 6 -l eng+equ -c tessedit_char_whitelist=0123456789+-÷x --tessdata-dir {tess_dir}"
        text: str = pytesseract.image_to_string(image, config=config)
        print(text)

        sequences = text.split("\n")
        result = 0

        try:
            for seq in sequences:
                if not seq:
                    continue
                operator, operand = seq[0], int(seq[1:])
                if operator == "+":
                    result += operand
                elif operator == "-":
                    result -= operand
                elif operator == "x":
                    result *= operand
                elif operator == "÷":
                    result //= operand
        except Exception as e:
            print(e)
            continue

        print("Result:", result)
        res = submit_solution(challenge, {"result": result})
        print(res)

        if res.get("accepted", False):
            break

    shutil.rmtree(tess_dir)


if __name__ == "__main__":
    main()
