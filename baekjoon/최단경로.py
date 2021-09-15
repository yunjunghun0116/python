import sys

def main():
    
    v,e = map(int,sys.stdin.readline().split())
    start = int(sys.stdin.readline())
    board = [[float('inf') for _ in range(v+1)]for __ in range(v+1)]
    board[start][start] = 0   
    for _ in range(e):
        start_index,end_index,value = map(int,sys.stdin.readline().split())
        board[start_index][end_index] = value

    for i in range(1,v+1):
        if board[start][i] != float('inf'):
            for j in range(1,v+1):
                if board[i][j] != float('inf'):
                    if board[start][j] > board[start][i]+ board[i][j]:
                        board[start][j] = board[start][i] + board[i][j]
    

    result = board[start][1:]
    for i in range(len(result)):
        if result[i] != float('inf'):
            print(result[i])
        else:
            print('INF')
         

    
if __name__ == '__main__':
    main()

