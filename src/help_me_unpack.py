from pathlib import Path
import base64
import struct

from utils import *


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    bytes_64 = base64.b64decode(res_json["bytes"])

    int_val = struct.unpack("i", bytes_64[0:4])[0]
    uint = struct.unpack("I", bytes_64[4:8])[0]
    short = struct.unpack("h", bytes_64[8:10])[0]
    # skip 2 bytes because of padding
    float_val = struct.unpack("f", bytes_64[12:16])[0]
    double = struct.unpack("d", bytes_64[16:24])[0]
    double_network = struct.unpack("!d", bytes_64[24:32])[0]

    solution = {
        "int": int_val,
        "uint": uint,
        "short": short,
        "float": float_val,
        "double": double,
        "big_endian_double": double_network,
    }
    print(solution)
    res = submit_solution(challenge, solution)
    print(res)


if __name__ == "__main__":
    main()
