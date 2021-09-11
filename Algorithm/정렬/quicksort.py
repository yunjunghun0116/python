import random

data_list = [];

for i in range(30):
    data_list.append(random.randint(0,999));

def quick_sort(list):
    if len(list) <= 1:
        return list
    left,right = [],[]

    pivot = list[0] #맨 앞의 요소를 피봇으로 설정
    for i in range(1,len(list)):
        if list[i] < pivot:
            left.append(list[i])
        else:
            right.append(list[i])

    #정렬된 left리스트 + 현재피봇을 배열화 한값+ 정렬된 right리스트 => 정렬된 전체 배열
    return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(data_list))

# 파이썬의 리스트간결화코드를 이용한 파이썬만가능한 퀵정렬코드
def quick_sort_listComprehension(list):
    if len(list) <= 1:
        return list
    
    pivot = list[0]

    left = [item for item in list[1:] if item < pivot]
    right = [item for item in list[1:] if item >= pivot]

    return quick_sort_listComprehension(left)+[pivot]+quick_sort_listComprehension(right)

print(quick_sort_listComprehension(data_list))

