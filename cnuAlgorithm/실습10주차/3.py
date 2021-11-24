import sys

def checkCnt(board,start,distance):
    # start에서 갈수있는 모든 도착점을 기준으로 최단거리를 기록한다.
    temp_board = board[:]
    for i in range(len(temp_board)):
        # inf의 값일경우 할필요 없기때문에 건너뛰고 실제값이 존재할경우 진행한다.
        if temp_board[start][i] != float('inf'):
            for j in range(len(temp_board)):
                if temp_board[i][j] != float('inf'):
                    # start -> j 거리보다 start -> i -> j의 거리가 더 가까우면 새로 업데이트해준다.
                    if temp_board[start][j] > temp_board[start][i]+ temp_board[i][j]:
                        temp_board[start][j] = temp_board[start][i] + temp_board[i][j]
    cnt = 0
    # max_distance보다 가까운 거리들만 카운팅한다
    for i in range(len(temp_board)):
        if board[start][i] <= distance:
            cnt+=1
            
    return cnt
    
    
def main():
    node_cnt,edge_cnt = map(int,sys.stdin.readline().strip().split())
    max_distance = int(sys.stdin.readline().strip())
    nodes = list(map(str,sys.stdin.readline().strip().split()))
    board = [[float('inf')for _ in range(node_cnt)]for _ in range(node_cnt)]
    # A -> A의 경우 0이기에 inf가 아닌 0으로 초기화해준다.
    for i in range(node_cnt):
        board[i][i] = 0
    for _ in range(edge_cnt):
        start,end,c = map(str,sys.stdin.readline().strip().split())
        cost = int(c)
        s = nodes.index(start)
        e = nodes.index(end)
        board[s][e] = cost
        board[e][s] = cost
        
    max_cnt = 0
    max_index = 0
    for i in range(node_cnt):
        temp_cnt = checkCnt(board,i,max_distance)
        # 받아온 cnt가 max_cnt보다 클경우 새로 업데이트해주고 index도 업데이트해준다.
        if max_cnt < temp_cnt:
            max_index = i
            max_cnt = temp_cnt
        
    print(nodes[max_index], max_cnt)
 
if __name__ == '__main__':
    main()