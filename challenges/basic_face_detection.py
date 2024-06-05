from pathlib import Path
from PIL import Image
from io import BytesIO
import numpy as np
import cv2

from utils import *

ROWS = COLS = 8


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    image_url = res_json["image_url"]

    b = requests.get(image_url).content
    image = Image.open(BytesIO(b))
    image.show()

    image_array = np.array(image)
    classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    height, width = image_array.shape
    w = width // ROWS  # width of a face tile
    h = height // COLS  # height of a face tile
    tiles = []

    for i in range(ROWS):
        for j in range(COLS):
            x = i * width // ROWS  # horizontal offset of current face tile
            y = j * height // COLS  # vertical offset of current face tile
            faces = classifier.detectMultiScale(
                image_array[y : y + h, x : x + w], scaleFactor=1.1, minNeighbors=5
            )
            if len(faces) > 0:
                tiles.append([i, j])

    print(tiles)
    res = submit_solution(challenge, {"face_tiles": tiles})
    print(res)


if __name__ == "__main__":
    main()
