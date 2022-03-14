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
    img_list = ['https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20210129_219%2F1611885704670Vh774_JPEG%2F155276_1.jpg&type=sc960_832',
        'https://contents.lotteon.com/itemimage/LO/14/30/64/30/56/_1/43/06/43/05/7/LO1430643056_1430643057_1.jpg/dims/optimize/dims/resizemc/400x400',
        'http://openimage.interpark.com/goods_image_big/7/2/7/0/7068487270e_l.jpg','http://openimage.interpark.com/goods_image_big/1/0/7/1/7455671071_l.jpg']
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