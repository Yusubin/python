import socket
#stream을 만들어야 하는데 한쪽으로만 흘러감......보내는 소켓이 따로 있고 받는 소켓이 따로 있음==>2개만들어야함
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind(('x', 3000))
print('x, 3000 port node start!')
print('------------B----------------')
while True:
    # pass
    #b가 a에게 받는 부분
    data, addr = sock2.recvfrom(1024)
    print('간단 채팅A>> ', data.decode('utf-8'))
    data = input("간단채팅B>> ")
    sock1.sendto(data.encode('utf-8'), ("192.168.0.7", 4000))