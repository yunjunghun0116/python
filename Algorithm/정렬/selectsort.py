import random

#최솟값을 찾아서 맨 앞에 배치, 그다음 최솟값을 찾아서 두번째에 배치 -> 버블정렬과는 다르게 맨처음부터 정렬된다.

data_list = [];

for i in range(30):
    data_list.append(random.randint(0,999));

for i in range(len(data_list)-1):
    #최솟값을 받을필요없이 확인(if문에서) 확인만해주면 된다. -> data_min(내 원래코드)을 없앰으로써 램효율을 높일수있다.
    data_min_index = i
    for j in range(i+1,len(data_list)):
        if data_list[j] < data_list[data_min_index]:
            data_min_index = j
    #파이썬에서 스왑해주는것은 temp를 사용할필요없이 이렇게 바로 해줄수있다.
    if data_min_index != i:
        data_list[i],data_list[data_min_index] = data_list[data_min_index],data_list[i]
        

print(data_list) 