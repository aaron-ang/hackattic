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
python3 src/<challenge>.py
```

## Challenges

- [collision_course](src/collision_course/collision_course.py)
- [backup_restore](src/backup_restore.py)
- [brute_force_zip](src/brute_force_zip.py)
- [dockerized_solutions](src/dockerized_solutions.py)
- [help_me_unpack](src/help_me_unpack.py)
- [hosting_git_repo](src/hosting_git.py)
- [jotting_jwts](src/jotting_jwts.py)
- [mini_miner](src/mini_miner.py)
- [password_hashing](src/password_hashing.py)
- [reading_qr](src/reading_qr.py)
- [tales_of_ssl](src/tales_of_ssl.py)
- [websocket_chit_chat](src/websocket_chit_chat.py)