"""
   依赖导入：
   如果导入的方法名有重复的，后面会覆盖先前的
"""

import time

time.sleep(2)

from time import sleep
sleep(2)

from time import *
from time import sleep as sl
sl(2)

from my_module1 import sum
print(sum(1,2,3,4,5))



