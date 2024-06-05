Challenge solutions to https://hackattic.com/

## Usage

1. Create a `.env` file with the following variables:

```
ACCESS_TOKEN=<your access token>
NGROK_AUTHTOKEN=<your ngrok authtoken (optional, for jotting_jwts challenge)>
```

2. Activate the virtual environment:

```bash
conda activate
```

2. Install the requirements:

```bash
pip install -r requirements.txt
```

3. Run the challenge solution:

```bash
python3 challenges/<challenge>.py
```

## Challenges

- [ ] [A global presence](challenges/a_global_presence.py)
- [x] [Collision course](challenges/collision_course/collision_course.py)
- [x] [Backup restore](challenges/backup_restore.py)
- [x] [Basic face detection](challenges/basic_face_detection.py)
- [x] [Brute force zip](challenges/brute_force_zip.py)
- [ ] [Dockerized solutions](challenges/dockerized_solutions.py)
- [x] [Help me unpack](challenges/help_me_unpack.py)
- [ ] [Hosting git](challenges/hosting_git.py)
- [x] [Jotting JWTs](challenges/jotting_jwts.py)
- [x] [Mini miner](challenges/mini_miner.py)
- [x] [Password hashing](challenges/password_hashing.py)
- [x] [Reading QR](challenges/reading_qr.py)
- [ ] [Serving DNS](challenges/serving_dns.py)
- [x] [Tales of SSL](challenges/tales_of_ssl.py)
- [ ] [The one with Redis](challenges/the_redis_one.py)
- [ ] [Touch-Tone dialing](challenges/touch_tone_dialing.py)
- [ ] [Visual basic math](challenges/visual_basic_math.py)
- [x] [Websocket chit chat](challenges/websocket_chit_chat.py)
