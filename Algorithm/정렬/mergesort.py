import random

# 시간복잡도
# 각 단계는 항상 O(n) -> 깊이(depth) : n/2^depth
# 매 깊이마다 2^i 개만큼의 원소가 존재하고,
# 그 존재들만큼 연산을 진행해주어야하므로 2^i * n/2^i  이므로 2^i 가 서로 소거되고, n만 남게된다.

data_list = [];

for i in range(30):
    data_list.append(random.randint(0,999));

# 내가 직접 짠 코드
def merge_sort(list):
    if len(list) <= 1:
        return list

    mid_index = int(len(list)/2)
    left = merge_sort(list[:mid_index])
    right = merge_sort(list[mid_index:])
    result = []
    left_index = 0
    right_index = 0
    #하나라도 len(left/right)와 left/right_index가 같으면 그때부턴 while문 종료
    while left_index != len(left) and right_index != len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index+=1
        else:
            result.append(right[right_index])
            right_index+=1
    if left_index == len(left):
        result = result + right[right_index:]
    else:
        result = result + left[left_index:]
    return result

# 알고리즘 강의 코드
# 함수2개 필요 -> 1. 분할, 2. 합병
def split(list):
    if len(list) <= 1:
        return list
    mid = int(len(list)/2)
    left = split(list[:mid])
    right = split(list[mid:])

    return merge(left,right)

def merge(left,right):
    result = []
    left_index = 0
    right_index = 0
    while left_index != len(left) and right_index != len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index+=1
        else:
            result.append(right[right_index])
            right_index+=1
    if left_index == len(left):
        result = result + right[right_index:]
    else:
        result = result + left[left_index:]
    return result


    
print(split(data_list))