import sys

# 파이썬에 스택은 없지만 배열을 통해 스택의 기능을 이용한 dfs과정

def main():
    #입력받는과정
    #0,0 -> m-1,n-1까지
    m,n = map(int,sys.stdin.readline().split())
    data = []
    for i in range(m):
        str = sys.stdin.readline()
        append_data = []
        for j in range(n):
            append_data.append(int(str[j]))
        data.append(append_data)

    visited_data = [[0 for j in range(n)]for i in range(m)]
    #data 에 제대로 들어가있음
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    result = []
    result.append((0,0))
    visited_data[0][0] = 1

    while result:
        x,y = result.pop(0)
        if x == m-1 and y == n-1:
            print(visited_data[x][y])
            break
        for i in range(4):
            tox = x + dx[i]
            toy = y + dy[i]
            if tox >= 0 and tox < m and toy >= 0 and toy < n:
                if visited_data[tox][toy] == 0 and data[tox][toy] == 1:
                    visited_data[tox][toy] = visited_data[x][y] + 1
                    result.append((tox,toy))



if __name__ == '__main__':
    main()

