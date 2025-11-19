import requests
from time import sleep as sl
import os
from capsol import getcap

def upload_to_scribd(fnamei):
    ss = str(os.getenv("SCRIBD_SESSION"))
    cookies = {
        '_scribd_session': ss,
        'scribd_ubtc':'u%3D23ead9e0-6c05-4d0e-bb7c-9a491ab12a0c%26h%3D6NqVGzii36qUZ%2BZkTcp94Hb6bxubtNgieFMIOsBbO9w%3D'
    }

    headers = {
        'x-csrf-token': '85QOR15lXUcLPC6NnxT1-Sj5sapPR79fJCOzWE_qlyvESm7oP6OhxPYiMOoB2-VtXjveY6gRoM-kwWAsvxGpMA',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'original_filename': 'lolmaiop.pdf',
    }

    response = requests.post('https://www.scribd.com/newupload/presigned_upload', cookies=cookies, headers=headers, data=data)

    respjs = response.json()["fields"]

    upload_url = response.json()["upload_url"]
    fname = response.json()["fields"]["key"]
    with open(fnamei,'rb') as f:
        files = {'file': ('ahj.pdf', f, 'application/pdf')}
        # send form fields as data and the file as files
        response2 = requests.post(upload_url, data=respjs, files=files)

    print(response2.status_code)

    return fname