import random

#맨뒤에서부터 정렬이 된다 -> 처음에 걸린최댓값이 마지막인덱스, 두번째걸린최댓값이 마지막에서두번째인덱스,

data_list = [];

for i in range(30):
    data_list.append(random.randint(0,999));

for i in range(len(data_list)-1):
    swap=False
    for j in range(len(data_list)-i-1):
        if data_list[j] > data_list[j+1]:
            data_list[j],data_list[j+1] = data_list[j+1],data_list[j]
            swap=True
    if swap ==False:
        break;

print(data_list) 