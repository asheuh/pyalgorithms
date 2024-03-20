import pprint
import os
import random
from random import Random
import requests
from z3 import *

from itertools import permutations
from dotenv import load_dotenv
from time import time
from pyalgorithms.cryptography.mersenne_twister import MersenneTwister

load_dotenv()

def make_api_call(payload, cookies):
    host = 'https://hack.ainfosec.com/challenge/submit-answer/'
    try:
        res = requests.post(host, data=payload, cookies=cookies)
        return res
    except Exception as e:
        raise e

def crack2fa():
    payload = {
        "csrfmiddlewaretoken": os.environ.get("CSRFMIDDLEWARETOKEN"),
        "challenge_id": "secure_otp",
    }

    cookies = {
        "csrftoken": os.environ.get("CSRFTOKEN"),
        "sessionid": os.environ.get("SESSIONID")
    }

    while True:
        otp = '123456' 
        payload['answer'] = otp
        print('Get the seed from first fail')
        res = make_api_call(payload, cookies)
        seed = res.json().get('hc_challenge', {}).get('seed')
        mt = MersenneTwister()
        random.seed(seed)
        state = random.getstate()
        random.setstate(state)

        print('Seed ===>', seed)
        otp = ''
        print()
        for i in range(6):
            otp += str(random.randint(0, 9))

        payload['answer'] = otp
        print('Trying current OTP ===>', otp)
        print()
        res = make_api_call(payload, cookies)
        if res.status_code in [200, 201]:
            print('SUCCESS')
            return otp
        break
    return 'Failed'

if __name__ == "__main__":
    result = crack2fa()
    print('FOUND ===>', result)
    
