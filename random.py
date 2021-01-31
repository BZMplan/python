import random
random.seed(123)
a = int(input("请输入一个整数:"))

b = int(random.randint(0,a*4))

print("您生成的随机数为:",b)