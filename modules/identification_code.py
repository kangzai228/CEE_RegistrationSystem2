# 识别验证码
import base64
import ddddocr
import logging

def identification_code(image_base64):
    image_bytes=base64.b64decode(image_base64)
    ocr = ddddocr.DdddOcr(show_ad=False)
    res = ocr.classification(image_bytes)
    logging.info(res)
    filename='code'+'.jpeg'
    with open('codes/'+filename, 'wb') as f:
        f.write(image_bytes)
    return res