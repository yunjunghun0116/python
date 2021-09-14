import sys

def main():

    N = int(sys.stdin.readline())
    board =  [list(map(int,sys.stdin.readline().split())) for _ in range(N)] 
    
    max = 0
    dx = [0,0,1,1]
    dy = [0,1,0,1]
    for i in range(N-1):
        for j in range(N-1):
            temp = 0
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                temp += board[x][y]
            if temp >= max:
                max = temp
            
    
    print(max)
    
if __name__ == '__main__':
    main()

