import os
import sys
import tkinter
import urllib
from tkinter import *
import tkinter.filedialog as tkfd
import requests
from PIL import Image, ImageTk

API_url = 'https://dapi.kakao.com/v2/vision/product/detect'
MYAPP_KEY = 'df5989bfdeb66e539382f8c9a0275d74'
class Fullscreen_Window(Tk):

    def __init__(self):
        self.tk = Tk()
        self.tk.geometry("500x1000")
        self.tk.title('상품검출을 이용한 옷추천')
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("f", self.toggle_fullscreen)
        self.tk.bind("e", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
def detect_product(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    try:
        data = {'image_url': image_url}
        resp = requests.post(API_url, headers=headers, data=data)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

def tag_product1(image_url):
    re=[]
    detection_result = detect_product(image_url)
    info_result = detection_result['result']
    object_re = info_result['objects']
    for i in object_re:
        re.append(i['class'])
    return re

def set_img():
    global entered_img
    entered_img = Image.open(entry.get())
    user_img = ImageTk.PhotoImage(entered_img)
    user_label = Label(w, image=user_img)
    user_label.image = user_img
    user_label.place(x=10, y=200)

def find_user_tag():
    global entered_img
    img_path = entry.get()
    global user_tag

    header = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}
    file = {'image': open(img_path, 'rb')}
    try:
        response = requests.post(API_url, headers=header, files=file)
        json_result = response.json()
        result = json_result['result']
        photo = result['objects']
        for i in photo:
            user_tag.append(i.get('class'))


    except Exception as e:
        print(str(e))
        sys.exit(0)

def search():
    print("search실행")
    global user_tag
    print(user_tag)
    image_url = [

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
        file = open('recommended2.txt', 'w')
        recommended_list = []
        for i in image_url:
            a = tag_product1(i)
            # 이미지에서 하나씩 태그 추출
            count=0
            for k in a: #각 사지 태그의 요소의 아이템  #['tote bag', 'one-piece', 'sandals', 'sandals', 'shirts'] 중 tote bag
                if k in user_tag:#요소의 아이템중 usertag에 해당하는게 있는가
                    count += 1

            if(count>=2):#요소의 아이템중 usertag에 해당하는게 2개이상 있을경우
                recommended_list.append(i)  #추천리스트에 추가


        r = set(recommended_list)
        list_r = list(r)

        for j in list_r:
            file.write(j + '\n')
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


def read():
    print("read")
    imgLabel=[]
    try:
        read_file = open('recommended2.txt', 'r')
        count=0
        while True:
            line= read_file.readline()
            if not line: break
            print(line)
            data="C:/Users/hi/Python/pythonProject8/openAPI/test"+str(count)+".jpg"
            urllib.request.urlretrieve(line,data)
            count+=1

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
            read_file.close()
        except:
            print("파일 닫는데 문제가 생김")
        read_file.close()
    show()

def show():
    # read()
    print("show")
    global img_url
    for i in range (0,5,1):
        img_url ="C:/Users/hi/Python/pythonProject8/openAPI/test"+str(i)+".jpg"
        img_url1=Image.open(img_url)
        user_img = ImageTk.PhotoImage(img_url1)
        user_label = Label(w, image=user_img)
        user_label.image = user_img
        user_label.place(x=10, y=200)

if __name__ == '__main__':
    user_tag=[]
    w = Fullscreen_Window()
    entry_guide = Label(w,
               text='사진 선택',
               font=('comic sans', 20)

               )
    entry_guide.pack()  # id라는 라벨을 w에 넣어줌
    entry = Entry(w)
    entry.pack()
    # re_frame = tkinter.Frame(w, bd=5)
    # re_frame.pack(side=tkinter.LEFT)
    path = tkfd.askopenfilename(initialdir="/", title="Select file",
                                filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    entry.insert('0', path)
    s = Button(w, text='set',
               command=set_img)
    s.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)
    b = Button(w, text='옷 검색',
               command = lambda : [find_user_tag(), search(), read()])
    b.pack(side=TOP, fill=X, ipadx=10, ipady=10, padx=10, pady=10)

    w.tk.mainloop()

