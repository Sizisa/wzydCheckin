import checkin
import requests
import os

def send(sckey,title,msg):
    url='http://sc.ftqq.com/%s.send'%(sckey)
    data={'text':title,'desp':msg}
    r=requests.post(url=url,data=data)
    print('server酱返回信息：'+r.text)


if __name__ == "__main__":
    sckey = os.environ['sckey']
    params = os.environ['params']

    result=checkin.checkin(params)

    if result[0]==0:
        send(sckey,'王者营地签到信息通知','签到成功！<br>今日奖励：'+result[1]+'<br>已连续签到'+result[2]+'天')
    elif result[0]==-1:
        send(sckey,'王者营地签到失败通知',result[1])
    else:
        send(sckey,'王者营地签到失败通知',result[1])