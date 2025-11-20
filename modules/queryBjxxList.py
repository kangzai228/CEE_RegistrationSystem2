# 获取班级列表
import requests
def queryBjxxList(ticketNO,bmddm):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'https://jxgk.jxeea.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://jxgk.jxeea.cn/ksbm/cxtj/kscx/kscx',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="142", "Microsoft Edge";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'ticketNO': ticketNO,
    }

    data = {
        'bmddm': bmddm,
    }

    response = requests.post('https://jxgk.jxeea.cn/ksy/ksbm/api/v2/admin/common/queryBjxxList.rest', headers=headers, data=data)
    # print(response.json()["data"])
    banjiList=[]
    for i in response.json()["data"]:
        banjiList.append(i["bjdm"])
    return banjiList

if __name__ == '__main__':
    bmddm='36073101'
    ticketNO='7de8cc6a8fb40df7514ca0775f7dd1a4a00c242143411e4c606ea2a2da4908a67c376a337d2cd0ec0c5309fa1aa5756f7ce772010cd41fb61ac23491ccf67c91'
    banjiList=queryBjxxList(ticketNO,bmddm)
    print(banjiList)