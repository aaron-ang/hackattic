from pathlib import Path
import base64
import zlib
import subprocess
import tempfile
import psycopg

from utils import *

DB_NAME = "hackattic"


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    dump_base64 = str(res_json["dump"])
    dump_bytes = unzip_dump(dump_base64)
    create_db()
    restore_dump(dump_bytes)
    ssns = get_alive_ssns()
    print(ssns)
    res = submit_solution(challenge, solution={"alive_ssns": ssns})
    print(res)
    drop_db()


def unzip_dump(dump_base64: str):
    dump_bytes = base64.b64decode(dump_base64)
    dump_bytes = zlib.decompress(dump_bytes, 15 + 32)
    return dump_bytes


def create_db():
    try:
        ps_drop = subprocess.run(
            [
                "dropdb",
                "--if-exists",
                DB_NAME,
            ]
        )
        assert ps_drop.returncode == 0
        ps_create = subprocess.run(
            [
                "createdb",
                DB_NAME,
            ]
        )
        assert ps_create.returncode == 0
    except Exception as e:
        print(e)


def drop_db():
    try:
        process = subprocess.run(
            ["dropdb", "-f", DB_NAME],
        )
        assert process.returncode == 0
    except Exception as e:
        print(e)


def restore_dump(dump: bytes):
    with tempfile.NamedTemporaryFile() as f:
        f.write(dump)
        try:
            process = subprocess.run(
                ["psql", "-d", DB_NAME, "-f", f.name],
            )
            assert process.returncode == 0
        except Exception as e:
            print(e)


def get_alive_ssns():
    res = []
    with psycopg.connect(f"dbname={DB_NAME}") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT ssn FROM criminal_records WHERE status = 'alive'")
            res = [row[0] for row in cur.fetchall()]
            conn.commit()
    return res


if __name__ == "__main__":
    main()
