import sys

def main():
    str_a = sys.stdin.readline().strip()
    str_b = sys.stdin.readline().strip()
    
    board = [[0 for _ in range(len(str_b)+1)]for _ in range(len(str_a)+1)]
    # a길이만큼의 행/ b길이만큼의 열
    # 겹치는 개수를 하나하나 찾되 이제껏 최대길이가 몇인지를 i-1,j-1로 판단한다.
    # 아닐경우 어차피 값은 같은행의 왼쪽 혹은 같은 열의 위쪽의 최댓값을 가져오면된다
    for i in range(1,len(str_a)+1):
        for j in range(1,len(str_b)+1):
            if str_a[i-1] == str_b[j-1]:
                board[i][j] = board[i-1][j-1] + 1
            else:
                board[i][j] = max(board[i][j-1],board[i-1][j])
    print(board[-1][-1])
    
if __name__ == '__main__':
    main()
    