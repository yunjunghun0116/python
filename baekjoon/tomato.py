import sys
from collections import deque
# 파이썬에 스택은 없지만 배열을 통해 스택의 기능을 이용한 dfs과정
# 7576

def main():
    # 입력받는과정
    m,n = map(int,sys.stdin.readline().split())
    data = []
    for i in range(n):
        append_data = list(map(int,sys.stdin.readline().split()))
        data.append(append_data)
    # data 에 제대로 들어가있음
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    data_queue = deque()
    tomatoCount = 0 # 0인 토마토 개수파악
    first_1_cnt = 0 # 이미 익은 토마토의 개수
    cnt = 0
    # 알고리즘
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                data_queue.append([i,j])
                # 맨 처음의 1인 토마토 개수는 제외해야하기때문에 한번 세준다
                first_1_cnt+=1
            elif data[i][j] == 0:
                tomatoCount += 1
    flag = True

    checkTomatoCount = 0 # 몇개의 토마토를 건드렸는지
    while flag:
        size = len(data_queue)
        for i in range(size):
            get_data = data_queue.popleft()
            checkTomatoCount+=1
            x = get_data[0]
            y = get_data[1]
            for j in  range(4):
                tox = x + dx[j]
                toy = y + dy[j]
                if tox >= 0 and tox < n and toy >= 0 and toy < m : 
                    if data[tox][toy] == 0 :
                        data[tox][toy] = 1
                        data_queue.append([tox,toy])
        if len(data_queue) == 0:
            flag = False
        else:
            cnt += 1


    if checkTomatoCount - first_1_cnt == tomatoCount:
        print(cnt)
    else:
        print(-1)
        



if __name__ == '__main__':
    main()

