import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solve(board,size):
    result = []

    def dfs(row,col):
        stack = []
        board[row][col] = 0
        stack.append((row,col))
        cnt = 1
        while stack:
            x,y = stack.pop()
            for i in range(4):
                tx = x + dx[i]
                ty = y + dy[i]
                if tx >= 0 and tx < size and ty >= 0 and ty < size:
                    if board[tx][ty] == 1:
                        board[tx][ty] = 0
                        cnt += 1
                        stack.append((tx,ty))
        return cnt
        
    for i in range(size):
        for j in range(size):
            if board[i][j] == 1:
                result.append(dfs(i,j))
    
    return result


def main():
    size = int(sys.stdin.readline().strip())
    board = []
    for _ in range(size):
        board.append(list(map(int,sys.stdin.readline().strip())))
    
    result = solve(board,size)
    length = len(result)
    result.sort()
    print(length)
    for i in range(length):
        print(result[i])
    

if __name__ == '__main__':
    main()

