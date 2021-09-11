from math import fabs
import random

# SuquentialSearch : 순차탐색
# 데이터가 담긴 리스트를 앞에서부터 하나하나 비교해가며 원하는 데이터를 찾는방법

data_list = [];

for i in range(30):
    data_list.append(random.randint(0,99));

def sequentialSearch(list,data):
    for i in range(len(list)):
        if list[i] == data:
            return i
    return -1

print(data_list)
print(sequentialSearch(data_list,77))