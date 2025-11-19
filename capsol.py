# https://github.com/2captcha/2captcha-python

# RecaptchaV2EnterpriseTaskProxyless
import time
import requests
import os
def getcap():
    ss = os.environ.get('SCRIBD_SESSION')
    params = {
        'googlekey': "6LdS1x0TAAAAAEhPxj6ivlWEgdLcSGD-pocphPJs",
        'pageurl': "https://www.scribd.com/upload-document",
        'method': 'userrecaptcha',
        # 'invi'
        'key': os.getenv('2CAPTCHA_KEY')
    }
    endpoint = 'http://2captcha.com/in.php'
    response = requests.post(endpoint, params=params)
    # print(response.text)

    params = {
                'id': response.text.split('|')[1],
                'action': 'get',
                'key': str(os.environ.get('CAPTCHA_KEY'))
            }
    endpoint = 'http://2captcha.com/res.php'
    response2 = requests.get(endpoint, params=params)
    while 'CAPCHA_NOT_READY' in response2.text:
        time.sleep(5)
        response2 = requests.get(endpoint, params=params)
        print(response2.text)
    captcha_token = response2.text.split('|')[1]
    cookies = {
        '_scribd_session': ss,
        'scribd_ubtc':'u%3D23ead9e0-6c05-4d0e-bb7c-9a491ab12a0c%26h%3D6NqVGzii36qUZ%2BZkTcp94Hb6bxubtNgieFMIOsBbO9w%3D'
    }
    headers = {
        'x-csrf-token': '85QOR15lXUcLPC6NnxT1-Sj5sapPR79fJCOzWE_qlyvESm7oP6OhxPYiMOoB2-VtXjveY6gRoM-kwWAsvxGpMA',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    veriurl = "https://www.scribd.com/newupload/captcha_token"
    res = requests.post(veriurl,data={"g-recaptcha-response":captcha_token},cookies=cookies,headers=headers)
    return res.json()["token"]

