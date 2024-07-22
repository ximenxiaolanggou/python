"""
   自定义包

"""

import chapter_01.fun
count = chapter_01.fun.sum(1,2,3)
print(count)

from chapter_01 import fun
count = fun.sum(1,2,3)
print(count)

from chapter_01.fun import sum
count = sum(1,2,3)
print(count)

