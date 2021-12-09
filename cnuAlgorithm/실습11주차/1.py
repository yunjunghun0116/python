import sys


def main():
    result_weight = [float('inf')]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    row,col,weight = map(int,sys.stdin.readline().strip().split())
    board = []
    visited = [[False for _ in range(col)]for _ in range(row)]
    for i in range(row):
        input_data = sys.stdin.readline()
        lists = ' '.join(input_data)
        board.append(lists.split())
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'S' or board[i][j] == 'E':
                board[i][j] = 0
                continue
            else:
                board[i][j] = int(board[i][j])
            
    def dfs(board,curx,cury,curweight,visited):
        if curx==col-1 and cury == row-1:
            if result_weight[-1] > curweight:
                result_weight.append(curweight)
        
        else:
            for i in range(4):
                x = curx+dx[i]
                y = cury+dy[i]
                if x >= 0 and x < col and y >= 0 and y < row and visited[y][x]==False:
                    visited[y][x] = True
                    if(curweight+board[y][x] < result_weight[-1]):
                        dfs(board,x,y,curweight+board[y][x],visited)
                    visited[y][x] = False
    visited[0][0] = True
    dfs(board,0,0,0,visited)
    if(result_weight[-1] == float('inf') or weight-result_weight[-1] < 0):
        print('FAIL')
    else:
        print(weight-result_weight[-1])


if __name__ == '__main__':
    main()
    