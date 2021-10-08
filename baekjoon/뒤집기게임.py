import sys

row_result = []
row_cnt_result = []
col_result = []
col_cnt_result = []
def dfs(board,size,current,cnt):
    if len(current) == size:
        row_result.append(current[:])
        row_cnt_result.append(cnt)
        return
    curr_row = len(current)
    current_board = current[:]
    row_list = board[curr_row][:]
    current_board.append(row_list)
    dfs(board,size,current_board,cnt)
    row_list_swap = [1-row_list[i] for i in range(size)]
    current_board.pop()
    current_board.append(row_list_swap)
    dfs(board,size,current_board,cnt+1)

def col_change(board,size,current,cnt):
    if len(current[0]) == size:
        col_result.append(current[:])
        col_cnt_result.append(cnt)
        return
    curr_col = len(current[0])
    current_board = current[:]
    for i in range(size):
        current_board[i].append(board[i][curr_col])
    col_change(board,size,current_board,cnt+1)
    for i in range(size):
        current_board[i][curr_col] = 1 - current_board[i][curr_col]
    col_change(board,size,current_board,cnt+1)


def main():
    size = int(sys.stdin.readline())
    board = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(size)]
    
    dfs(board,size,[],0)

    for i in range(len(row_result)):
        print(i,'번째')
        for j in range(size):
            print(row_result[i][j])
        

    for i in range(len(row_result)):
        start_col = [[] for _ in range(size)]
        col_change(row_result[i],size,start_col,0)
    
    for i in range(len(col_result)):
        for j in range(size):
            print(col_result[i][j])


    
        


if __name__ == '__main__':
    main()

