length = int(input())

max = 0
min = 10000000000

for i in range(0, length):
    current_num = int(input())
    if(current_num > max):
        max = current_num
    if(current_num < min):
        min = current_num

village_length = max - min
print(village_length)
