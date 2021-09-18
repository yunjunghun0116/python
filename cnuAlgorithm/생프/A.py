import sys

def main():
    size = int(sys.stdin.readline())
    board = [[' 'for _ in range(size)]for _ in range(size)]
    cnt = 1
    for i in range(1,size-1):
        board[i][cnt],board[i][size-1-cnt] = '*','*'
        cnt+=1
    for i in range(size):
        if i == 0 or i == size-1:
            board[i] = ['*' for _ in range(size)]
        else:
            board[i][0],board[i][size-1] = '*','*'
    result = []
    for i in range(size):
        result.append(''.join([str(_)for _ in board[i]]))
    for i in range(size):
        print(result[i])

    
if __name__ == '__main__':
    main()