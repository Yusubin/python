import sys
import argparse
from collections import Counter

import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/product/detect'
MYAPP_KEY = 'b5478bb850b34bb812aeb0b91fca2774'


def detect_product(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    try:
        data = {'image_url': image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)


def tag_product(image_url, re):
    detection_result = detect_product(image_url)
    info_result = detection_result['result']
    object_re = info_result['objects']
    for i in object_re:
        re.append(i['class'])
    return re


def tag_product1(image_url):
    re=[]
    detection_result = detect_product(image_url)
    info_result = detection_result['result']
    object_re = info_result['objects']
    for i in object_re:
        re.append(i['class'])
    return re


if __name__ == "__main__":


    ## 사용자의 입력을 받는 부분 ##
    user_list= [ ]
    while True:
        u=input("이미지 주소를 입력")
        if(u=="1"):break
        user_list.append(u)

    user_re = []  # 사용자가 입력한 이미지의 태그의 결과를 저장할 리스트
    for i in user_list:
        tag_product(i, user_re)  # 이미지에서 하나씩 태그 추출
    user_tag = Counter(user_re)

    print(user_tag)

    image_url = [
        'https://static.coupangcdn.com/image/vendor_inventory/c2ba/ec493de1c1ebd60e7c2914908433ce638b6e01cc9a0091f444b59daba2ee.jpg',
        'https://contents.lotteon.com/itemimage/LO/14/30/64/30/56/_1/43/06/43/05/7/LO1430643056_1430643057_1.jpg/dims/optimize/dims/resizemc/400x400',
        'http://openimage.interpark.com/goods_image_big/7/2/7/0/7068487270e_l.jpg',
        'http://openimage.interpark.com/goods_image_big/1/0/7/1/7455671071_l.jpg',
        'http://thumbnail.10x10.co.kr/webimage/image/basic600/367/B003676360.jpg?cmd=thumb&w=400&h=400&fit=true&ws=false',
        'https://i.pinimg.com/550x/12/30/45/123045ca40e5aae6b4b5eb9d4fc163da.jpg',
        'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8344080%2F83440803122.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20210129_219%2F1611885704670Vh774_JPEG%2F155276_1.jpg&type=sc960_832',
        'https://shop1.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop1.daumcdn.net%2Fshophow%2Fp%2FA5102502258.jpg%3Fut%3D20210413222430',
        'https://i.pinimg.com/474x/9d/4e/40/9d4e40244932b1e19c794f07fcb4c7a6.jpg',
        'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8344080%2F83440803122.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220228_225%2F1646013317542CI13R_JPEG%2F47149100723352490_2010556781.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_2979480%2F29794808846.1.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220218_84%2F1645126021422HNy7M_JPEG%2F46261856044409370_1633666740.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20220228_225%2F1646013317542CI13R_JPEG%2F47149100723352490_2010556781.jpg&type=sc960_832',
        'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fscontent-icn1-1.cdninstagram.com%2Fvp%2F8ef5cd3b518b6234f40193e4649aa59a%2F5D4B2254%2Ft51.2885-15%2Ffr%2Fe15%2Fs1080x1080%2F53267140_125177811879131_3535660168275939536_n.jpg%3F_nc_ht%3Dscontent-icn1-1.cdninstagram.com&type=sc960_832',
        'https://chic-line.com/web/emoz88/2022/01SP/CLMAO062/00_06.jpg',
        'https://chic-line.com/web/emoz88/2022/01SP/CLMAO062/CLMAO062_02.jpg',
        'https://shopping-phinf.pstatic.net/main_3088161/30881617771.20220211012324.jpg?type=f640',
        'https://shopping-phinf.pstatic.net/main_2948027/29480270215.20211031213251.jpg?type=f640',
        'https://static.coupangcdn.com/image/vendor_inventory/c2ba/ec493de1c1ebd60e7c2914908433ce638b6e01cc9a0091f444b59daba2ee.jpg',
        'https://contents.lotteon.com/itemimage/LO/14/30/64/30/56/_1/43/06/43/05/7/LO1430643056_1430643057_1.jpg/dims/optimize/dims/resizemc/400x400',
        'http://openimage.interpark.com/goods_image_big/7/2/7/0/7068487270e_l.jpg',
        'http://openimage.interpark.com/goods_image_big/1/0/7/1/7455671071_l.jpg',
        'http://thumbnail.10x10.co.kr/webimage/image/basic600/367/B003676360.jpg?cmd=thumb&w=400&h=400&fit=true&ws=false',
        'https://i.pinimg.com/550x/12/30/45/123045ca40e5aae6b4b5eb9d4fc163da.jpg',
        'https://search.pstatic.net/common/?src=https%3A%2F%2Fshopping-phinf.pstatic.net%2Fmain_8344080%2F83440803122.jpg&type=sc960_832',
        'https://search.pstatic.net/common/?src=http%3A%2F%2Fshop1.phinf.naver.net%2F20210129_219%2F1611885704670Vh774_JPEG%2F155276_1.jpg&type=sc960_832',
        'https://shop1.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop1.daumcdn.net%2Fshophow%2Fp%2FA5102502258.jpg%3Fut%3D20210413222430',
        'https://i.pinimg.com/474x/9d/4e/40/9d4e40244932b1e19c794f07fcb4c7a6.jpg'
    ]

    try:
        file = open('recommended.txt', 'w')
        recommended_list = []
        re = []  # 사용자가 입력한 이미지의 태그의 결과를 저장할 리스트
        for i in image_url:
            a = tag_product1(i)  # 이미지에서 하나씩 태그 추출
            for k in a:
                if (k == user_re[0]):
                    recommended_list.append(i)
                    file.write(i+'\n')



    except NameError:
        print("해당 이름의 파일을 찾을수없음")
    except FileNotFoundError:
        print("해당 파일을 찾을수없음")
    except IOError:
        print("읽고 쓰는데 문제가 생김")
    except:
        print("파일을 처리하는데 문제가 생겼음")
    finally:
        try:
            file.close()
        except:
            print("파일 닫는데 문제가 생김")
