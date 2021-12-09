import sys

def main():
    max_weight = int(sys.stdin.readline().strip())
    size = int(sys.stdin.readline().strip())
    # 가로 weight 세로 item
    item_weight = list(map(int,sys.stdin.readline().strip().split()))
    item_value = list(map(int,sys.stdin.readline().strip().split()))
    board = [[0 for _ in range(max_weight+1)] for _ in range(size+1)]

    for i in range(1,size+1):
        for j in range(1,max_weight+1):
            if j < item_weight[i-1]:
                board[i][j] = board[i-1][j]
            else:
                # 이차원배열로 생각할때 여기가 중요한데
                # 여기를 보면 이때까지 현재 weight - item_weight의 최댓값+item_value 와
                # 이때까지의 현재weight까지의 최댓값중 뭐가더큰지를 업데이트
                board[i][j] = max(board[i-1][j],board[i-1][j-item_weight[i-1]]+item_value[i-1])
    print(board[size][max_weight])
if __name__ == '__main__':
    main()
    