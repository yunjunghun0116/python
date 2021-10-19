import sys

cnt = 0


dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
def solve(board,lenx,leny,lenz):
    # (z,y,x) 를 사용 z : k층, y : 몇번째, x : 자세한 원소
    # 저장 : z층, y개, 각 원소를 x를 통해서 나타냄
    global dx,dy,dz,cnt
    my_stack = []
    for i in range(lenz):
        for j in range(leny):
            for k in range(lenx):
                if board[i][j][k] == 1:
                    my_stack.append((i,j,k))
    
    while len(my_stack) != 0:
        stack_len = len(my_stack)
        isAppend = False
        temp_stack = [] # 새로 stack 에 집어넣을 원소를 넣는 공간
        for _ in range(stack_len):
            z,y,x = my_stack.pop()
            for i in range(6):
                t_z = z + dz[i]
                t_y = y + dy[i]
                t_x = x + dx[i]
                if t_z >= 0 and t_z < lenz and t_y >= 0 and t_y < leny and t_x >= 0 and t_x < lenx:
                    if  board[t_z][t_y][t_x] == 0:
                        isAppend = True
                        board[t_z][t_y][t_x] = 1
                        temp_stack.append((t_z,t_y,t_x)) #바로 stack에 append해줄경우 pop은 맨 마지막원소를 빼오기때문에 제대로작동이안된다.
        for i in range(len(temp_stack)):
            my_stack.append(temp_stack[i])
        if isAppend:
            cnt+=1


def check(board,lenx,leny,lenz):
    for i in range(lenz):
        for j in range(leny):
            for k in range(lenx):
                if board[i][j][k] == 0:
                    return False
    return True
    

def main():
    m,n,h = map(int,sys.stdin.readline().strip().split())
    # (z,y,x) 로 해야함
    board = [[[]for _ in range(n)]for _ in range(h)]
    # z,y,x식으로 저장
    for z in range(h):
        for y in range(n):
            board[z][y] = list(map(int,sys.stdin.readline().strip().split()))
    solve(board,m,n,h)
    if check(board,m,n,h):
        print(cnt)
    else:
        print(-1)
    
if __name__ == '__main__':
    main()

