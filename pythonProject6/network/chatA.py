import socket
#stream을 만들어야 하는데 한쪽으로만 흘러감......보내는 소켓이 따로 있고 받는 소켓이 따로 있음==>2개만들어야함
sock1=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP, 보내는용
sock2=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #받는용...
sock1.bind(("192.168.0.7", 4000))
print("192.168.0.7 :  4000 port node start___ ")
print("________________A________________ ")
while True:
    data=input("간단채팅A>> ")
    sock1.sendto(data.encode('utf-8'), ("192.168.0.7", 3000))

    data, addr = sock2.recvfrom(1024)
    print('간단 채팅B>> ', data.decode('utf-8'))