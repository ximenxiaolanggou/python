"""
   异常
"""

try:
    1/0
except (ZeroDivisionError, NameError) as e:
    print("出现ZeroDivisionError或者NameError异常")
except Exception as e:
    print("出现异常", e)
else:
    print("没有出现异常")
finally:
    print("finally 代码")


