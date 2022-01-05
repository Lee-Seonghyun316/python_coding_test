def make_array(n):
    answer = []
    for i in range(len(n)):
        answer.append(int(n[i]))
    return answer


num_list = input()
num_list = make_array(num_list)
sum = 0
for num_item in num_list:
    if(num_item == 0):
        continue
    elif(num_item == 1):
        sum += num_item
    else:
        if(sum == 0):
            sum = 1
        sum *= num_item

print(sum)
