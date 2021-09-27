import sys

def dfs(queen,n,row):
    count = 0
    if n == row:
        return 1
    
    # 가로로 한번만 진행
    for col in range(n):
        queen[row] = col
        # for-else구문
        for x in range(row):
            # 세로로 겹치면 안됨
            if queen[x] == queen[row]: 
                break
            # 대각선으로 겹치면 안됨
            if abs(queen[x]-queen[row]) == (row-x):
                break
        else:
            count += dfs(queen, n, row+1)
            
    return count


def main():
    n = int(sys.stdin.readline())
    queen = [0] * n
    print(dfs(queen,n,0))


if __name__ == '__main__':
    main()




