num_list = list(map(int, input().split()))
print(num_list)

max_up = 0
max_down = 0

if(num_list[0] < num_list[1]):
    befroe_up = True
else:
    befroe_up = False

count_up = 1
count_down = 1

for i in range(1, len(num_list)+1):
    if(num_list[i] == -1):
        break
    else:
        if(num_list[i] < num_list[i+1]):
            current_up = True
            if(befroe_up == current_up):
                count_up += 1
                if(max_up < count_up):
                    max_up = count_up
            else:
                if(max_up < count_up):
                    max_up = count_up
                count_up = 1
            befroe_up = current_up
        elif(num_list[i] > num_list[i+1]):
            current_up = False
            if(befroe_up == current_up):
                count_down += 1
                if(max_down < count_down):
                    max_down = count_down
            else:
                if(max_down < count_down):
                    max_down = count_down
                count_down = 1
            befroe_up = current_up

print(max_up, count_down)
