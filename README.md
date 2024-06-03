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

- [ ] [a_global_presence](challenges/a_global_presence.py)
- [x] [collision_course](challenges/collision_course/collision_course.py)
- [x] [backup_restore](challenges/backup_restore.py)
- [ ] [basic_face_detection](challenges/basic_face_detection.py)
- [x] [brute_force_zip](challenges/brute_force_zip.py)
- [ ] [dockerized_solutions](challenges/dockerized_solutions.py)
- [x] [help_me_unpack](challenges/help_me_unpack.py)
- [ ] [hosting_git](challenges/hosting_git.py)
- [x] [jotting_jwts](challenges/jotting_jwts.py)
- [x] [mini_miner](challenges/mini_miner.py)
- [x] [password_hashing](challenges/password_hashing.py)
- [x] [reading_qr](challenges/reading_qr.py)
- [ ] [serving_dns](challenges/serving_dns.py)
- [x] [tales_of_ssl](challenges/tales_of_ssl.py)
- [ ] [the_redis_one](challenges/the_redis_one.py)
- [ ] [touch_tone_dialing](challenges/touch_tone_dialing.py)
- [ ] [visual_basic_math](challenges/visual_basic_math.py)
- [x] [websocket_chit_chat](challenges/websocket_chit_chat.py)
