import sys
import argparse
from tkinter import messagebox

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

    return label_kr
if __name__ == '__main__':
    img_list = ['https://w.namu.la/s/5d5ec65c290284aa95363cc3b26b78dfb14d30739dd299c6728c016421eed661245d23776d22eb478b2bca6445c862bf74262298d4240ec3d5c6c27cb0ae3d47e58c0f61e2578f154acef752d5abfe62358659674438039be10fad1d48c6513a',
                'https://cdn.mindgil.com/news/photo/202102/70718_6733_1648.jpg',
                'https://images.chosun.com/resizer/CYshmV-b5T3_NfHX6Yt5JVwRsu8=/616x0/smart/cloudfront-ap-northeast-1.images.arcpublishing.com/chosun/4K4JOARBMZD5HDYI47WK72W7VQ.jpg']
    result_list = []
    for img in img_list:
        label_result = multi_tag(img)
        result_list += label_result
    print(result_list)

    # from collections import Counter
    count_result = Counter(result_list)
    print(count_result)
    # Counter({'사람': 3, '여러사람': 3, '여성': 3, '남성': 3, '바지': 3, '안경': 1, '스포츠': 1, '실외': 1, '모자': 1})
    print(count_result.get('안경'))
    # 1
    print(count_result.most_common(1))
    # [('사람', 3)]
    print(count_result.most_common(5))
    # [('사람', 3), ('여러사람', 3), ('여성', 3), ('남성', 3), ('바지', 3)]
    order_5 = count_result.most_common(5)
    print(order_5[0])  # ('사람', 3)
    order_1 = order_5[0]
    print('제일 빈도수가 높은 단어는 ', order_1[0],
          '이고, 빈도수는 ', order_1[1]
          )

    if order_1[0]=='사람':
        tour = '놀이공원'
    elif order_1[0]=='남성':
        tour = '등산'
    else:
        tour='제주도'
    data='당신에게 '+tour+"을 추천합니다~~!"
    messagebox.showinfo('추천',data)