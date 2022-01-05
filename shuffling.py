import random

num_list = list()
max = int(input())
num = random.randrange(1, max+1)
num_list.append(num)
if(num < max and num > 1):
    num = random.randrange(num, max+1)
    num_list.append(num)
    num = random.randrange(1, num)
    num_list.append(num)
    if()
