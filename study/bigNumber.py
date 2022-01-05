# 8:41
# 큰 수의 법칙
# 두개 수 입력받아 M N K
# N 번 더하는데 K번 반복가능 (어떤 원소)
# M 개 배열 주어짐
# 반복물 돌면서, 가장 큰수 2개 찾음
# O(M)
# M/K+1 번 * (K*가장큰수 + 두번째 큰수 ) + M%(k+1)*가장큰수
# + 상수 번
# 시간 복잡도 가능
array_len, plus_num, repeat_num = map(int, input().split())
num_array = list(map(int, input().split()))
max_first = 0
max_second = 0
for num_item in num_array:
    if(num_item > max_first):
        max_second = max_first
        max_first = num_item
    else:
        continue
print(max_first, max_second)
result = (int(plus_num/(repeat_num+1)) * (repeat_num*max_first +
          max_second) + (plus_num % (repeat_num+1)) * max_first)
print(result)
