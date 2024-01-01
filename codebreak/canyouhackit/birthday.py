import pprint
import os
import requests

from dotenv import load_dotenv

load_dotenv()


def make_api_call(payload, cookies):
    host = 'https://hack.ainfosec.com/challenge/submit-answer/'
    try:
        res = requests.post(host, data=payload, cookies=cookies)
        return res
    except Exception as e:
        raise e

def crackbirthday():
    payload = {
        "csrfmiddlewaretoken": os.environ.get("CSRFMIDDLEWARETOKEN"),
        "challenge_id": "birthday",
    }

    cookies = {
        "csrftoken": os.environ.get("CSRFTOKEN"),
        "sessionid": os.environ.get("SESSIONID")
    }
    cmonth = 6
    cdate = 10
    cyear = 1991
    result = '06/07/1991'

    while True:
        if cdate < 1:
            cmonth -= 1
            cdate = 31

        if cmonth < 1:
            cyear -= 1
            cmonth = 12
            cdate = 31

        if cyear < 1950:
            print('FAILED!')
            break

        result = f"{0 if len(str(cmonth)) == 1 else ''}{cmonth}/{0 if len(str(cdate)) == 1 else ''}{cdate}/{cyear}"
        payload['answer'] = result
        print('CHECKING CURRENT DATE ==>', result)
        res = make_api_call(payload, cookies)

        if res.status_code in [200, 201]:
            print('SUCCESS!')
            break

        cdate -= 1
    return result

if __name__ == '__main__':
    result = crackbirthday()
    print('FOUND BIRTHDAY ===>', result)
