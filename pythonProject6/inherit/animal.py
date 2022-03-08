class Animal:
    name=''

    def __init__(self,name):
        self.name=name
    #self=생성된 객체 주소.
    #a1=Animal('hong')
    #a1.name='gonh

    #기능(객체가 생성된후 호출이 가능)
    #객체가 생성되면 주소가 생김
    #주소가 있어야 함수 호출이 가능하다
    #객체가 생성이 되고 주소가 있어야 이기능을 쓸수있다. (함수호출을 할수있다.)
    #a1.move()
    def move(self):
        print('move!!')

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):#재사용 (상속)
        print("멍멍")#재정의
class Duck(Animal):
    def speak(self):
        print("꽥꽥")