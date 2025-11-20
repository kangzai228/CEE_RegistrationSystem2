# 管理员登录
import requests

def ssoLogin(username, password,code,captchaId):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'https://jxgk.jxeea.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://jxgk.jxeea.cn/admin/login',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'username': username,
        'password': password,
        'code': code,
        'captchaId': captchaId,
    }

    response = requests.post('https://jxgk.jxeea.cn/bdss/system/api/sso/sso/ssoLogin.rest', headers=headers, data=data)
    # print(response.json()["data"])
    return response.json()["data"]["ticket"]["keyNO"]
