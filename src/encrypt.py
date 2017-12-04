import base64
import json

import urllib3
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

CHAR_SET = 'utf-8'


def get_public_key():
    http_pool = urllib3.PoolManager()
    response = http_pool.request("GET", "http://localhost:18888/security/rsaPublicKey")
    res = json.loads(response.data)
    print(res)
    data = res['data']
    public_key = data['publicKey']
    key_id = data['keyId']
    public_key = "-----BEGIN PUBLIC KEY-----\n" + public_key + "\n-----END PUBLIC KEY-----"
    return key_id, public_key


def rsa_encode(public_key, text):
    public_key = RSA.importKey(public_key)
    rsa_encoder = PKCS1_v1_5.new(public_key)
    text = str(base64.b64encode(rsa_encoder.encrypt(text.encode(CHAR_SET))), CHAR_SET)
    return text


def encode(text):
    key_id, public_key = get_public_key()
    text = rsa_encode(public_key, text)
    return key_id, text
