"""
 多线程
"""

import threading
import time
def dance(msg):
   while True:
       print(msg)
       time.sleep(1)


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing, args = ("我要唱歌 ~~",))
    dance_thread = threading.Thread(target=dance, args = ("我要跳舞 ~~",))

    sing_thread.start()
    dance_thread.start()