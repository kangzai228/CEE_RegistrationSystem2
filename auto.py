from account import account,ticketNo

from modules.captcha import captcha
from modules.identification_code import identification_code
from modules.ssoLogin import ssoLogin
from modules.queryBmRelatedRight import queryBmRelatedRight

from ticketNo import ticketNo
def auto(username, password):
    captchaData = captcha()
    captchaId, captchaImg = captchaData['captchaId'], captchaData['captcha']
    # print(captchaImg,captchaId)
    image_base64=captchaImg.split(',')[1]
    print(image_base64)
    code=identification_code(image_base64)
    print(code)
    #===================================
    username=account['username']
    password=account['password']


if __name__ == '__main__':
    username = 'your_username'
    password = 'your_password'
    auto(username, password)