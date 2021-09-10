import random

#맨처음데이터는 냅두고 두번째인덱스부터 시작,
#현재인덱스를 기준으로 앞으로 넘어가며 계속 확인하는데 어느 인덱스를 기준으로 자기보다 크면 앞으로 넘어간다.

data_list = [];

for i in range(30):
    data_list.append(random.randint(0,999));

for i in range(1,len(data_list)):
    #for문사용시
    for j in range(i,0,-1):
        if data_list[j-1]<=data_list[j]:
            break
        else:
            data_list[j-1],data_list[j] = data_list[j],data_list[j-1]

    #while문 사용시
    cur_index = i
    while cur_index != 0:
        #코딩을 할때 항상 예외처리를 먼저 해준다음 예외의 경우를 통과했을때 코드를 진행해주는방식으로 진행하자
        if data_list[cur_index-1]<=data_list[cur_index]:
            break
        else:
            data_list[cur_index-1],data_list[cur_index] = data_list[cur_index],data_list[cur_index-1]
            cur_index-=1
        

print(data_list) 