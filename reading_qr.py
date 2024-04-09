from pathlib import Path
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

from utils import *


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    image = requests.get(res_json["image_url"]).content
    qr_decoder = cv2.QRCodeDetector()
    retval, points, straight_qrcode = qr_decoder.detectAndDecode(
        np.array(Image.open(BytesIO(image)))
    )
    print(retval)
    res = submit_solution(challenge, {"code": retval})
    print(res)


if __name__ == "__main__":
    main()
