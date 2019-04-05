import requests

for id in range(1, 100):
    url = f'http://192.168.0.100/Accounts/Details?id={id}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.107',
        'Accept-Language': 'en-GB',
    }

    r = requests.get(url, headers=headers)
    pounds = r.text.replace('\n', ' ').split('&pound;')[1].split(' ')[0]
    print(id, pounds)
