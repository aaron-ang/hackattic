import sys
from pathlib import Path
from PIL import Image
from io import BytesIO
import easyocr
import random

FILE_DIR = Path(__file__).parent
sys.path.append(FILE_DIR.parent.as_posix())

from utils import *


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    image_url = res_json["image_url"]

    b = requests.get(image_url).content
    image = Image.open(BytesIO(b)).convert("L")
    image.show()

    reader = easyocr.Reader(["en"])
    texts: list[str] = reader.readtext(b, allowlist="0123456789+-x÷", detail=0)
    print(texts)

    result = 0
    operators = ["+", "-", "x", "÷"]
    for t in texts:
        first = t[0]
        if first in operators:
            operator = first
            operand = int(t[1:])
        else:
            operator = "-"
            operand = int(t)

        # small hack since OCR does not recognize `÷`
        if operator == "+" and random.uniform(0, 1) < 0.5:
            operator = "÷"

        print(operator, operand)
        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "x":
            result *= operand
        elif operator == "÷":
            result //= operand
        operator = ""
        operand = 0

    print("Result:", result)
    res = submit_solution(challenge, {"result": result})
    print(res)


if __name__ == "__main__":
    main()
