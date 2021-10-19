import sys

dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]

def solve(board,width,height):
    result_cnt = 0
    def dfs(row,col):
        stack = []
        stack.append((row,col))
        board[row][col] = -1            
        while stack:
            x,y = stack.pop()
            for i in range(8):
                tx = x + dx[i]
                ty = y + dy[i]
                if tx >= 0 and tx < height and ty >= 0 and ty < width:
                    if board[tx][ty] == 1:
                        board[tx][ty] = -1
                        stack.append((tx,ty))
    for i in range(height):
        for j in range(width):
            if board[i][j] == 1:
                result_cnt += 1
                dfs(i,j)
    return result_cnt


def main():
    result = []
    while True:
        width,height = map(int,sys.stdin.readline().strip().split())
        board = []
        if width == 0 and height == 0:
            break
        for _ in range(height):
            board.append(list(map(int,sys.stdin.readline().strip().split())))
        result.append(solve(board,width,height))
    for i in range(len(result)):
        print(result[i])
    

if __name__ == '__main__':
    main()

