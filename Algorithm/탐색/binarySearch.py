import random

# 이진탐색의 전제조건 : 모든 원소는 정렬되어있다

data_list = [];

for i in range(30):
    data_list.append(random.randint(0,99));

data_list.sort()

# 내가짠 코드
def binarySearch(list,data):
    if len(list) < 1:
        return False

    mid = int(len(list)/2)
    if data == list[mid]:
        return True
    elif data < list[mid] :
        return binarySearch(list[:mid],data)
    elif data > list[mid]:
        return binarySearch(list[mid+1:],data)
    else:
        return False

# 강의코드
def binary_search(data,search):
    print(data)
    if len(data) == 1:
        if search == data[0]:
            return True
        else:
            return False
    if len(data) < 1:
        return False

    medium = len(data)//2
    if search == data[medium]:
        return True
    else:
        if search > data[medium]:
            return binary_search(data[medium:],search)
        else:
            return binary_search(data[:medium],search)


print(data_list)
print(binary_search(data_list,77))
