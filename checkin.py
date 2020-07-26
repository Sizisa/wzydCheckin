import requests




def checkin(params):
    res = requests.post(url='https://ssl.kohsocialapp.qq.com:10001/play/h5sign', data=params, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    print(res.text)
    state = res.json()
    print(state)