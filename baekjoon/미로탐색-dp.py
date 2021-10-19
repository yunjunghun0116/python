import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]
min_result = float('inf')
def dfs(board,visited,x,y,height,width,cnt):
    if x == height-1 and y == width -1:
        global min_result
        min_result = min(min_result,cnt)
        return
    isVisited = visited[:]
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx >= 0 and tx < height and ty >= 0 and ty < width and board[tx][ty] == 1 and visited[tx][ty] == 0:
            isVisited[tx][ty] = 1
            dfs(board,isVisited,tx,ty,height,width,cnt+1)
            isVisited[tx][ty] = 0

def main():
    height,width = map(int,sys.stdin.readline().strip().split())
    board = []
    visited = [[0 for _ in range(width)]for _ in range(height)]
    for _ in range(height):
        board.append(list(map(int,''.join(sys.stdin.readline().strip().split()))))

    dfs(board,visited,0,0,height,width,1)
    print(min_result)

if __name__ == '__main__':
    main()

