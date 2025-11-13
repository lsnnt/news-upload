import requests
from time import sleep as sl
import os


def upload_to_scribd(fnamei):
    ss = str(os.getenv("SCRIBD_SESSION"))
    cookies = {
        '_scribd_session': ss,
    }

    headers = {
        'x-csrf-token': 'DHttpQ_a1BDQc6FH1fuhOTnOPaUtkef8GNPr9VC6Du07pQ0Kbhwoky1tvyBLNLGtTwxSbMrH-GyYMTiBoEEw9g',
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

    print(response2.text)

    params = {
        'sig': '8d266c092bd1e6cc814d48adfe31d44426e477e8',
        'user_id': '688308679',
    }

    data = {
        'session_val': ss,
        'filename': fname,
        'original_filename': fnamei.split("/")[-1]
    }

    response3 = requests.post(
        'https://www.scribd.com/newupload/direct_upload',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )

    print(response3.text)
    theid = response3.json()["id"]
    sp = response3.json()["secret_password"]

    urld = f"https://www.scribd.com/document_downloads/{str(theid)}?secret_password={sp}&extension=pdf"
    return urld

