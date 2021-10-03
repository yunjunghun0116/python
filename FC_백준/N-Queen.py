import sys

def dfs(n,cur_col,result):
    # row : int, col : array
    if len(cur_col) == n :
        result.append(cur_col[:])
    for i in range(n):
        #열이 겹치지않음
        col_len = len(cur_col)
        for j in range(col_len):
            if cur_col[j] == i:
                break
            if (col_len - j) == abs(cur_col[j]-i):
                break
        else:
            cur_col.append(i)
            dfs(n,cur_col,result)
            cur_col.pop()
    return result
            



def main():
    n = int(sys.stdin.readline())
    result = []
    print(len(dfs(n,[],result)))

if __name__ == '__main__':
    main()

