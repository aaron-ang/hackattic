from pathlib import Path
from operator import itemgetter
from pycountry import countries
from cryptography.hazmat.primitives import serialization, hashes
import base64
from cryptography import x509
import pendulum

from utils import *


def main():
    challenge = Path(__file__).stem
    res_json = get_challenge(challenge)
    private_key: str = res_json["private_key"]
    domain, serial_number, country = itemgetter("domain", "serial_number", "country")(
        res_json["required_data"]
    )
    print(
        f"private_key: {private_key}\ndomain: {domain}\nserial_number: {serial_number}\ncountry: {country}"
    )

    cert = generate_cert(private_key, domain, serial_number, country)
    res = submit_solution(challenge, {"certificate": cert})
    print(res)


def generate_cert(private_key, domain, serial_number, country):
    try:
        country_alpha_2 = countries.search_fuzzy(country)[0].alpha_2
    except LookupError:
        pass
    country_alpha_2 = get_country_by_alpha_2(country)
    if not country_alpha_2:
        raise ValueError(f"Country {country} not found")

    now = pendulum.now(tz="UTC")

    key = serialization.load_der_private_key(base64.b64decode(private_key), None)

    subject = issuer = x509.Name(
        [
            x509.NameAttribute(x509.OID_COUNTRY_NAME, country_alpha_2),
            x509.NameAttribute(x509.OID_COMMON_NAME, domain),
        ]
    )

    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(int(serial_number, base=16))
        .not_valid_before(now)
        .not_valid_after(now.add(months=13))
        .sign(key, hashes.SHA256())
    )

    return base64.b64encode(cert.public_bytes(serialization.Encoding.DER)).decode()


def get_country_by_alpha_2(country):
    if country == "Tokelau Islands":
        return "TK"
    elif country == "Christmas Island":
        return "CX"
    elif country in ("Cocos Islands", "Keeling Islands"):
        return "CC"
    elif country == "Sint Maarten":
        return "CK"
    else:
        return None


if __name__ == "__main__":
    main()
