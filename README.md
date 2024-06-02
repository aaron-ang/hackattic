Challenge solutions to https://hackattic.com/

## Usage

1. Create a `.env` file with the following variables:

```
ACCESS_TOKEN=<your access token>
NGROK_AUTHTOKEN=<your ngrok authtoken (optional, for collision_course challenge)>
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

- [collision_course](challenges/collision_course/collision_course.py)
- [backup_restore](challenges/backup_restore.py)
- [brute_force_zip](challenges/brute_force_zip.py)
- [dockerized_solutions](challenges/dockerized_solutions.py)
- [help_me_unpack](challenges/help_me_unpack.py)
- [hosting_git_repo](challenges/hosting_git.py)
- [jotting_jwts](challenges/jotting_jwts.py)
- [mini_miner](challenges/mini_miner.py)
- [password_hashing](challenges/password_hashing.py)
- [reading_qr](challenges/reading_qr.py)
- [tales_of_ssl](challenges/tales_of_ssl.py)
- [websocket_chit_chat](challenges/websocket_chit_chat.py)
