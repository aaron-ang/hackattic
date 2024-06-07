import sys
from pathlib import Path
from PIL import Image
from io import BytesIO
import pytesseract

FILE_DIR = Path(__file__).parent
sys.path.append(FILE_DIR.parent.as_posix())

from utils import *


def main():
    while True:
        challenge = Path(__file__).stem
        res_json = get_challenge(challenge)
        image_url = res_json["image_url"]

        b = requests.get(image_url).content
        image = Image.open(BytesIO(b)).convert("L")
        # image.show()

        config = f"--psm 6 -l eng+equ -c tessedit_char_whitelist=0123456789+-÷x --tessdata-dir {FILE_DIR / 'tessdata_best'}"
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


if __name__ == "__main__":
    main()
