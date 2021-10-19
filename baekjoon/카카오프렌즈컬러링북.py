import sys
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def main():
    board = []
    result = []
    def dfs(row,col,val,width,height):
        cnt = 1
        stack = []
        stack.append((row,col))
        board[row][col] = -1
        while stack:
            x,y = stack.pop()
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if tx >= 0 and tx < width and ty >= 0 and ty < height:
                    if board[tx][ty] == val:
                        board[tx][ty] = -1
                        cnt += 1
                        stack.append((tx,ty))
        result.append(cnt)


    m,n = map(int,sys.stdin.readline().strip().split())
    for _ in range(m):
        board.append(list(map(int,sys.stdin.readline().strip().split())))
    for i in range(m):
        for j in range(n):
            if board[i][j] > 0:
                dfs(i,j,board[i][j],m,n)
    print(len(result))
    print(max(result))

if __name__ == '__main__':
    main()

