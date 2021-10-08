import sys

row_result = []
row_cnt_result = []
# 행렬 전환후에
changed_result = []

col_result = []
col_cnt_result = []

final_result = []

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

def row_col_change(board,size):
    temp_board = [[board[i][j] for j in range(size)]for i in range(size)]
    for i in range(size):
        for j in range(i+1):
            temp = temp_board[i][j]
            temp_board[i][j] = temp_board[j][i]
            temp_board[j][i] = temp
    return temp_board

def col_change(board,size,current,cnt):
    if len(current) == size:
        col_result.append(current[:])
        col_cnt_result.append(cnt)
        return
    curr_row = len(current)
    current_board = current[:]
    row_append = board[curr_row][:]
    current_board.append(row_append)
    col_change(board,size,current_board,cnt)
    row_list_swap = [1 - row_append[i] for i in range(size)]
    current_board.pop()
    current_board.append(row_list_swap)
    col_change(board,size,current_board,cnt+1)

def check(board,size,cnt):
    cnt_0 = 0
    cnt_1 = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                cnt_0 += 1
            if board[i][j] == 1:
                cnt_1 += 1
    final_cnt = cnt + min(cnt_0,cnt_1)
    final_result.append(final_cnt)
    
def main():
    size = int(sys.stdin.readline())
    board = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(size)]
    dfs(board,size,[],0)
    for i in range(len(row_result)):
        temp_result = row_col_change(row_result[i],size)
        changed_result.append(temp_result)
    # 여기까지 행렬변환 성공
    for i in range(len(row_result)):
        curr_board = changed_result[i]
        curr_cnt = row_cnt_result[i]
        col_change(curr_board,size,[],curr_cnt)
    # col_result에는 모든 경우의 수가 저장
    # col_cnt_result = 모든 cnt가 저장
    for i in range(len(col_result)):
        check(col_result[i],size,col_cnt_result[i])

    print(min(final_result))

if __name__ == '__main__':
    main()

