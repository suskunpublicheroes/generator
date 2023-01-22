import os
import ecdsa
import requests

try:
    private_key = os.urandom(32).hex()
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()
    public_key = '04' + vk.to_string().hex()
    address = vk.to_p2pkh()
    url = f"https://blockchain.info/q/addressbalance/{address}"
    satoshi = int(requests.get(url).text)
    btc = satoshi / 10**8
    with open("success.txt", "a") as success:
        success.write(private_key+'\n')
        success.write(public_key+'\n')
        success.write(f'{btc} BTC'+'\n')

except:
    with open("fail.txt", "a") as fail:
        fail.write(private_key+'\n')
