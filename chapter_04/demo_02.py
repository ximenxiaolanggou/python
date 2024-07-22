"""
 网络编程
"""

import socket
import threading
import time

def create_socket_server():
    # 服务端
    socket_server = socket.socket()
    socket_server.bind(("192.168.111.101", 8888))
    socket_server.listen(1)  # 参数表示链接数量
    # conn 连接对象， address客户端地址信息
    print("等待客户端链接...")
    conn, address = socket_server.accept()
    print(f"连接成功，客户端信息：{address}")
    while True:
        # recv获取的是字符，通过decode转成字符串
        data = conn.recv(1024).decode("UTF-8")
        print(f"接收到客户端数据：{data}")
        conn.send("收到消息".encode("UTF-8"))
        #conn.close()
        #socket_server.close()

def create_socket_client():
    socket_client = socket.socket()
    socket_client.connect(("127.0.0.1", 8888))

    while True:
        socket_client.send("你好呀".encode("UTF-8"))
        data = socket_client.recv(1024).decode("UTF-8")
        print(f"接收到服务器消息：{data}")
        time.sleep(2)

if __name__ == '__main__':
    socket_server_thread = threading.Thread(target=create_socket_server)
    socket_server_thread.start()
    # create_socket_client()
    while True:
        pass

