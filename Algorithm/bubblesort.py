import random

data_list = [];

for i in range(30):
    data_list.append(random.randint(0,999));

for i in range(len(data_list)-1):
    for j in range(len(data_list)-i-1):
        if data_list[j] > data_list[j+1]:
            data_list[j],data_list[j+1] = data_list[j+1],data_list[j]

print(data_list) 