from pathlib import Path
import asyncio
from websockets.client import connect
import pendulum
import re

from utils import *


async def main(token):
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    token = res_json["token"]
    uri = f"wss://hackattic.com/_/ws/{token}"

    async for websocket in connect(uri):
        interval_start = pendulum.now()
        print("Opened new connection")

        async for message in websocket:
            received_at = pendulum.now()
            print(message)

            if message == "ping!":
                interval = received_at - interval_start
                interval_start = received_at
                interval_ms = int(interval.total_seconds() * 1000)
                print(f"Interval: {interval_ms}ms")
                interval_ms = get_nearest_interval(interval_ms)
                await websocket.send(str(interval_ms))

            elif message.startswith("congratulations!"):
                secret_key = re.search(r'"([^"]*)"', message).group(1)
                print(f"Secret key: {secret_key}")
                res = submit_solution(challenge, {"secret": secret_key})
                print(res)
                return


def get_nearest_interval(interval_ms):
    intervals = [700, 1500, 2000, 2500, 3000]
    nearest_interval = intervals[0]
    for i in intervals[1:]:
        if abs(i - interval_ms) < abs(nearest_interval - interval_ms):
            nearest_interval = i
    return nearest_interval


if __name__ == "__main__":
    asyncio.run(main())
