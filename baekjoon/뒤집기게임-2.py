import sys

def find_cnt_0(results,size):
    cnt = 0
    row_boards = results
    # 행마다도 진행해주어야한다.
    for i in range(size):
        is_row_changed = True
        for j in range(size):
            if results[i][j] == 0:
                is_row_changed  = False
                break
        if is_row_changed:
            row_boards[i] = [1-results[i][j] for j in range(size)]
            cnt += 1
    # 각 열마다 진행해줄거라서
    for i in range(size):
        sub_col = []
        for j in range(size):
            sub_col.append(row_boards[j][i])
        cnt_0 = 0
        cnt_else = 0 
        while True:
            for j in range(size):
                if sub_col[j]  == 0:
                    cnt_0 += 1
                else:
                    cnt_else += 1
            if cnt_else > cnt_0:
                cnt +=  1
                for j in range(size):
                    if sub_col[j] == 0:
                        sub_col[j] = 1
                    else:
                        sub_col[j] -= 1
                cnt_0 = 0
                cnt_else = 0
            else:
                break
        for j in range(size):
            cnt += sub_col[j]

    return cnt

def find_cnt_1(results,size):
    cnt = 0
    row_boards = results
    # 행마다도 진행해주어야한다.
    for i in range(size):
        is_row_changed = True
        for j in range(size):
            if results[i][j] == 0:
                is_row_changed  = False
                break
        if is_row_changed:
            row_boards[i] = [1-results[i][j] for j in range(size)]
            cnt += 1
    # 각 열마다 진행해줄거라서
    for i in range(size):
        sub_col = []
        for j in range(size):
            sub_col.append(row_boards[j][i])
        cnt_0 = 0
        cnt_else = 0 
        while True:
            for j in range(size):
                if sub_col[j]   == 0:
                    cnt_0 += 1
                else:
                    cnt_else += 1
            if cnt_else > cnt_0:
                cnt += 1
                for j in range(size):
                    if sub_col[j] == 0:
                        sub_col[j] = 1
                    else:
                        sub_col[j] -= 1
                cnt_0 = 0
                cnt_else = 0
            else:
                break
        for j in range(size):
            cnt += sub_col[j]
    
    return cnt

def row_change_0(row,size):
    sub_arr = row
    cnt_1 = 0
    cnt_0 = 0
    for i in range(size):
        if row[i] == 0:
            cnt_0 +=1
        else:
            cnt_1 += 1
    if cnt_1 > cnt_0:
        sub_arr = [1-i for i in sub_arr]
        result = [1 for _ in range(size)]
    else:
        result = [0 for _ in range(size)]
    
    for i in range(size):
        if sub_arr[i] == 0:
            continue
        else:
            result[i] += 1
    return result

def solve_0(board,size):
    result = []
    for i in range(size):
        result.append(row_change_0(board[i],size))
    return result

def row_change_1(row,size):
    sub_arr = row
    cnt_1 = 0
    cnt_0 = 0
    for i in range(size):
        if row[i] == 1:
            cnt_1 +=1
        else:
            cnt_0 += 1
    if cnt_0 > cnt_1:
        sub_arr = [1-i for i in sub_arr]
        result = [1 for _ in range(size)]
    else:
        result = [0 for _ in range(size)]
    
    for i in range(size):
        if sub_arr[i] == 1:
            continue
        else:
            result[i] += 1
    return result

def solve_1(board,size):
    result = []
    for i in range(size):
        result.append(row_change_1(board[i],size))
    return result

def main():
    size = int(sys.stdin.readline())
    board = []
    for _ in range(size):
        board.append(list(map(int,sys.stdin.readline().strip().split())))
    result_0 = solve_0(board,size)
    to_0 = find_cnt_0(result_0,size)

    result_1 = solve_1(board,size)
    to_1 = find_cnt_1(result_1,size)
    print(min(to_0,to_1))

if __name__ == '__main__':
    main()

