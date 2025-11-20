from account import account

from modules.captcha import captcha
from modules.identification_code import identification_code
from modules.password_encrypt import password_encrypt
from modules.ssoLogin import ssoLogin

from modules.queryBjxxList import queryBjxxList
from modules.queryKscxDataPager import queryKscxDataPager
from modules.queryBmRelatedRight import queryBmRelatedRight

def auto(username, password):
    print(username,password)
    captchaData = captcha()
    captchaId, captchaImg = captchaData['captchaId'], captchaData['captcha']
    print(captchaImg,captchaId)
    image_base64=captchaImg.split(',')[1]
    print(image_base64)
    code=identification_code(image_base64)
    print(code)
    en_pwd=password_encrypt(password)
    ticketNO=ssoLogin(username, en_pwd,code,captchaId)
    banjiList=queryBjxxList(ticketNO,username)
    for bjdm in banjiList:
        kshList=queryKscxDataPager(ticketNO,username,bjdm)
        print(kshList)
        for ksh in kshList:
            queryBmRelatedRight(ticketNO,ksh)
            break
        break

if __name__ == '__main__':
    username=account['username']
    password=account['password']
    auto(username, password)