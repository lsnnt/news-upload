from capsol import getcap
import requests
import os
def lr(flist,oflist):
    ss = str(os.getenv("SCRIBD_SESSION"))
    cookies = {
        '_scribd_session': ss,
        'scribd_ubtc':'u%3D23ead9e0-6c05-4d0e-bb7c-9a491ab12a0c%26h%3D6NqVGzii36qUZ%2BZkTcp94Hb6bxubtNgieFMIOsBbO9w%3D'
    }
    headers = {
        'x-csrf-token': '85QOR15lXUcLPC6NnxT1-Sj5sapPR79fJCOzWE_qlyvESm7oP6OhxPYiMOoB2-VtXjveY6gRoM-kwWAsvxGpMA',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    params = {
        'sig': '8d266c092bd1e6cc814d48adfe31d44426e477e8',
        'user_id': '688308679',
    }
    capt = getcap()
    for i in range(len(flist)):
        data = {
            'captcha_token': str(capt),
            'session_val': ss,
            'filename': flist[i],
            'original_filename': oflist[i].split("/")[-1]
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
        print(urld)
