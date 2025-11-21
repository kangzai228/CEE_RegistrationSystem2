#查询一个班的所有学生考生号
from modules.addToXLS import addToXLS

import requests
def queryKscxDataPager(ticketNO,bmddm,bjdm):
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
        'dsdm': '3607',
        'xqdm': '360731',
        'bmddm': bmddm,
        'bjdm': bjdm,# 班级代码
        'bmlbdm': '',
        'ksh': '',
        'zjhm': '',
        'xm': '',
        'mzdm': '',
        'zzmmdm': '',
        'wyyzdm': '',
        'jbkldm': '',
        'bylbdm': '',
        'xkkmdm': '',
        'ksztdm': '',
        'orderBy': 'ksh asc',
        'xqdsqy': '1',
        'limit': '100',
        'page': '1',
    }

    response = requests.post(
        'https://jxgk.jxeea.cn/ksy/ksbm/api/v2/admin/ksxxData/queryKscxDataPager.rest',
        headers=headers,
        data=data,
    )
    # print(response.json()["data"])
    kshList = []
    
    for i in response.json()["data"]:
        # print(i)
        kshList.append(i["ksh"])
        dataList=[]
        for key,value in i.items():
            dataList.append(value)
        addToXLS("./stu_info.xls",dataList)
    print("{}班共有{}人".format(response.json()["data"][0]['bjmc'],len(response.json()["data"])))
    return kshList