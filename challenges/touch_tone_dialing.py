import wave
import pyaudio
import numpy as np
from io import BytesIO
from pathlib import Path
from scipy.io import wavfile

from utils import *

DTMF = {
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


def play_wav(data: bytes):
    with wave.open(BytesIO(data), "rb") as wf:
        p = pyaudio.PyAudio()
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
        )
        while len(data := wf.readframes(1024)):
            stream.write(data)
        stream.close()
        p.terminate()


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    wav_url = res_json["wav_url"]

    b = requests.get(wav_url).content
    play_wav(b)

    rate: int
    data: np.ndarray
    rate, data = wavfile.read(BytesIO(b))
    duration = len(data) / rate
    interval = 0.06
    step = int(len(data) // (duration // interval))

    sequence = ""
    current = ""

    for i in range(0, len(data) - step, step):
        signal = data[i : i + step]
        frequencies = np.fft.fftfreq(signal.size, d=(1 / rate))
        fourier = np.fft.fft(signal)

        # Low
        i_min = np.where(frequencies > 0)[0][0]
        i_max = np.where(frequencies > 1050)[0][0]
        freq = frequencies[i_min:i_max]
        amp = abs(fourier.real[i_min:i_max])
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
        i_max = np.where(frequencies > 1600)[0][0]
        freq = frequencies[i_min:i_max]
        amp = abs(fourier.real[i_min:i_max])
        hf = freq[np.where(amp == max(amp))[0][0]]
        delta = 20
        best = 0

        for f in [1209, 1336, 1477]:
            if abs(hf - f) < delta:
                delta = abs(hf - f)
                best = f
        hf = best

        if lf == 0 or hf == 0:
            current = ""
        elif DTMF[(lf, hf)] != current:
            current = DTMF[(lf, hf)]
            sequence += current

    print(sequence)
    res = submit_solution(challenge, {"sequence": sequence}, playground=True)
    print(res)


if __name__ == "__main__":
    main()
