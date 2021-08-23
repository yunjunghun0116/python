import random

my_list = random.sample(range(100),30)

#뒤에서부터 정렬해오는 버블정렬
#앞에서부터 하나씩 비교하는 알고리즘.
def bubblesort(data):
    #마지막 인덱스까지 확인
    for i in range(len(data)-1):
        swap = False
        #처음부터 정렬되지않은 부분까지 확인
        for j in range(len(data)-i-1):
            if(data[j]>data[j+1]):
                data[j],data[j+1] = data[j+1],data[j]
                print(data)
                swap = True
        if swap == False:
            break
    return data

print(bubblesort(my_list))