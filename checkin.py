import datetime

import requests,os,json


if __name__ == '__main__':
#   pushplus token
    pkey = os.environ.get('PUSHPLUS','')
#   消息推送
    sendmsg = ''
#   GLaDOS cookie
    cookies = os.environ.get('COOKIES',[]).split('&')
    if cookies[0] == '':
        print('未获取到GLADOS_COOKIES环境变量')
        cookies = []
        exit(0)
    checkin_url = 'https://glados.rocks/api/user/checkin'
    status_url = 'https://glados.rocks/api/user/status'
    referrer = 'https://glados.rocks/console/checkin'
    origin = 'https://glados.rocks'
    useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    payload = {
        'token': 'glados.one'
    }
    for cookie in cookies:
        checkin = requests.post(checkin_url,
                                headers={'cookie':cookie,'referrer':referrer,'origin':origin,'user-agent':useragent,'content-type':'application/json; charset=utf-8'},data = json.dumps(payload))
        status = requests.get(status_url,headers={'cookie':cookie,'referrer':referrer,'origin':origin,'useragent':useragent})
        
        days = str(status.json()['data']['leftDays']).split('.')[0]
        email = status.json()['data']['email']

        balance = str(checkin.json()['list'][0]['balance']).split('.')[0]
        change = str(checkin.json()['list'][0]['change']).split('.')[0]

        if 'message' in checkin.text:
            msg = checkin.json()['message']
            print(email+'|'+'剩余：'+days+'天|'+msg+'|积分：'+balance+'|变化：'+ change +'\n')
            sendmsg += email+'|'+'剩余：'+days+'天|'+msg+'|积分：'+balance+'|变化：'+ change +'\n'
        else:
            sendmsg += email + '签到失败，请更新cookies'

    if pkey !='':
        requests.get( 'http://www.pushplus.plus/send?token=' + pkey + '&title=GLaDOS签到情况&content=' + sendmsg)








# import requests
# import json
# import os
# # -------------------------------------------------------------------------------------------
# # github workflows
# # -------------------------------------------------------------------------------------------
# if __name__ == '__main__':
#     # pushplus秘钥 申请地址 http://www.pushplus.plus
#     sckey = os.environ.get("PUSHPLUS", "")

#     # 推送内容
#     title = "Glados"
#     success, fail = 0, 0        # 成功账号数量 失败账号数量
#     sendContent = ""

#     # glados账号cookie 直接使用数组 如果使用环境变量需要字符串分割一下
#     cookies = os.environ.get("COOKIES", []).split("&")
#     if cookies[0] == "":
#         print('未获取到COOKIE变量')
#         cookies = []
#         exit(0)

#     url = "https://glados.rocks/api/user/checkin"
#     url2 = "https://glados.rocks/api/user/status"

#     referer = 'https://glados.rocks/console/checkin'
#     origin = "https://glados.rocks"
#     useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
#     payload = {
#         'token': 'glados.one'
#     }

#     for cookie in cookies:
#         checkin = requests.post(url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
#                                 'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
#         state = requests.get(url2, headers={
#                              'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
#     # --------------------------------------------------------------------------------------------------------#
#         if checkin.status_code == 200:
#             # 解析返回的json数据
#             result = checkin.json()     
#             # 获取签到结果
#             status = result.get('message')
            
#             success += 1
#             message_status = status
#         else:
#             email = ""
#             fail += 1
#             message_status = "签到请求url失败, 请检查..."
#             message_days = "获取信息失败"
        
#         if cookie == cookies[-1]:
#             sendContent += '-' * 30
        
#      # --------------------------------------------------------------------------------------------------------#
#     print("sendContent:" + "\n", sendContent)
#     if sckey != "":
#         title += f': 成功{success},失败{fail}'
#         plusurl = f"http://www.pushplus.plus/send?token={sckey}&title={title}&content={sendContent}"
#         r = requests.get(plusurl)
#         print(r.status_code)
