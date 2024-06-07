from pathlib import Path
from scipy.io import wavfile
from io import BytesIO
import numpy as np

from utils import *

dtmf = {
    (697, 1209): "1",
    (697, 1336): "2",
    (697, 1477): "3",
    (770, 1209): "4",
    (770, 1336): "5",
    (770, 1477): "6",
    (852, 1209): "7",
    (852, 1336): "8",
    (852, 1477): "9",
    (941, 1209): "*",
    (941, 1336): "0",
    (941, 1477): "#",
}


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    wav_url = res_json["wav_url"]

    b = requests.get(wav_url).content
    rate, data = wavfile.read(BytesIO(b))

    if len(data.shape) == 2:  # stereo
        data = data.sum(axis=1)

    precision = 0.075
    duration = len(data) / rate
    step = int(len(data) // (duration // precision))

    sequence = ""
    c = ""

    for i in range(0, len(data) - step, step):
        signal = data[i : i + step]
        frequencies = np.fft.fftfreq(signal.size, d=(1 / rate))
        amplitudes = np.fft.fft(signal)

        # Low
        i_min = np.where(frequencies > 0)[0][0]
        i_max = np.where(frequencies > 1050)[0][0]
        freq = frequencies[i_min:i_max]
        amp = abs(amplitudes.real[i_min:i_max])
        lf = freq[np.where(amp == max(amp))[0][0]]
        delta = 20
        best = 0

        for f in [697, 770, 852, 941]:
            if abs(lf - f) < delta:
                delta = abs(lf - f)
                best = f
        lf = best

        # High
        i_min = np.where(frequencies > 1100)[0][0]
        i_max = np.where(frequencies > 1970)[0][0]
        freq = frequencies[i_min:i_max]
        amp = abs(amplitudes.real[i_min:i_max])
        hf = freq[np.where(amp == max(amp))[0][0]]
        delta = 20
        best = 0

        for f in [1209, 1336, 1477]:
            if abs(hf - f) < delta:
                delta = abs(hf - f)
                best = f
        hf = best

        if lf == 0 or hf == 0:
            c = ""
        elif dtmf[(lf, hf)] != c:
            c = dtmf[(lf, hf)]
            sequence += c

    print(sequence)
    res = submit_solution(challenge, {"sequence": sequence})
    print(res)


if __name__ == "__main__":
    main()
