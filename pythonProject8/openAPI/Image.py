import sys
import argparse
import requests #알트+엔터(cmd+1)
from collections import Counter
import requests
from PIL import Image,ImageDraw, ImageFont

url = 'https://dapi.kakao.com/v2/vision/multitag/generate'
key = 'b5478bb850b34bb812aeb0b91fca2774'

def multi_tag(image_url):
    header = {'Authorization': 'KakaoAK {}'.format(key)}
    img_data = {'image_url': image_url}
    response = requests.post(url, headers=header, data=img_data)
    # print(response)
    json_result=response.json()
    # print(json_result)
    result=json_result['result']
    # print(result)
    label_kr=result['label_kr']
    print(label_kr)
if __name__ == '__main__':
    img_url = 'https://img.khan.co.kr/news/2019/11/29/l_2019112901003607500286631.jpg'
    multi_tag(img_url)
