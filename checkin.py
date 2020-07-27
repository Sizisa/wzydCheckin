import requests




def checkin(params):
    res = requests.post(url='https://ssl.kohsocialapp.qq.com:10001/play/h5sign', data=params, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    
    state = res.json()
    print(state)
    
    if state['result']==-1:    
        return (-1,state['returnMsg'],0)
    if state['result']==0:
        msg=state['data']['todayGift'].split('|')[1]
        return(0,msg,state['data']['userTotalSign'])
    return (999,res.text,0)