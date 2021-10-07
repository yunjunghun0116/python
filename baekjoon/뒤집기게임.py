import sys
white_make = 64
black_make = 64

def check_white(board,size):
    for i in range(size):
        for j in range(size):
            if board[i][j] == 1:
                return (False,i,j)
    return (True,0,0)

def check_black(board,size):
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                return (False,i,j)
    return (True,0,0)

def curr_change(board,size,row,col):
    changed_board = board
    changed_board[row][col] = 1 - changed_board[row][col]
    return changed_board
def row_change(board,size,row):
    changed_board = board
    for i in range(size):
        changed_board[row][i] = 1 - changed_board[row][i]
    return changed_board
def col_change(board,size,col):
    changed_board = board
    for i in range(size):
        changed_board[i][col] = 1 - changed_board[i][col]
    return changed_board


def make_white(board,size,cnt):# 모두 0인지
    check = check_white(board,size)
    global white_make
    if check[0] :
        white_make = min(white_make,cnt)
    else:
        if white_make <= cnt:
            return
        row,col = check[1],check[2]
        row_change_board = row_change(board,size,row)
        col_change_board = col_change(board,size,col)
        curr_change_board = curr_change(board,size,row,col)
        make_white(row_change_board,size,cnt+1)
        make_white(col_change_board,size,cnt+1)
        make_white(curr_change_board,size,cnt+1)

def make_black(board,size,cnt):
    check = check_black(board,size)
    global black_make

    if check :
        black_make = min(black_make,cnt)
    else:
        if black_make <= cnt:
            return
        row,col = check[1],check[2]
        row_change_board = row_change(board,row)
        col_change_board = col_change(board,col)
        curr_change_board = curr_change(board,row,col)
        make_black(row_change_board,size,cnt+1)
        make_black(col_change_board,size,cnt+1)
        make_black(curr_change_board,size,cnt+1)

def solve(board,size):
    global white_make
    global black_make
    make_white(board,size,0)
    make_black(board,size,0)

    return min(white_make,black_make)

def main():
    size = int(sys.stdin.readline().strip())
    board = []
    for _ in range(size):
        input_list = list(map(int,sys.stdin.readline().strip().split()))
        board.append(input_list)
    result = solve(board,size)
    print(result)

    

if __name__ == '__main__':
    main()

