import sys

def dfs(queen,n,currlength):
    #여기서 시작했을경우에 반환되는 모든 경우
    count = 0
    if n == currlength:
        return 1
    for i in range(n):
        #여기에서 쓰이는 for-else 구문은 for문도중 break로 걸러지지않을경우
        #else문을 진행한다는 의미
        queen[currlength] = i
        for j in range(currlength):
            if i == queen[j]:
                break
            if currlength - j == abs(queen[j] - i):
                break
        else:
            count += dfs(queen,n,currlength+1)
    #해당 위치를 기준으로 반환할수 있는 가능한 모든 queen의 count를 반환
    print(currlength,count)
    return count

def main():
    n = int(sys.stdin.readline())
    queen = [0 for _ in range(n)]
    print(dfs(queen,n,0))


if __name__ == '__main__':
    main()




