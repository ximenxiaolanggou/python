"""
    continue break
"""
num = 0
while True:
    if num == 10 :
        break
    num += 1
    print(num)

for num in range(10):
    if num % 2 == 1:
        continue
    print(f"{num},偶数")