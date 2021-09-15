import sys
from queue import PriorityQueue
def main():
    
    v,e = map(int,sys.stdin.readline().split())
    board = [[float('inf') for _ in range(v+1)]for __ in range(v+1)]
    for _ in range(0,e):
        start_index,end_index,value = map(int,sys.stdin.readline().split())
        board[start_index][end_index] = value
        board[end_index][start_index] = value
    v1_index,v2_index = map(int,sys.stdin.readline().split())

    def deijkstra(start):
        my_queue = PriorityQueue()
        dists = [float('inf') for _ in range(v+1)] #start에서 갈수있는 모든 거리를 나타내기위함
        dists[start] = 0
        my_queue.put((0,start))
        while not my_queue.empty():
            dist,index = my_queue.get()
            if dists[index] < dist:
                continue
            else:
                #dists[index] 가 내가 지금 뽑은 dist보다 크다는 말
                for i in range(1,v+1):
                    if dists[index]+board[index][i] < dists[i]:
                        dists[i] = dists[index]+board[index][i]
                        my_queue.put((dists[i],i))
                    else:
                        continue
        return dists

    
    one = deijkstra(1)[v1_index]+deijkstra(v1_index)[v2_index]+deijkstra(v2_index)[v]
    two = deijkstra(1)[v2_index]+deijkstra(v2_index)[v1_index]+deijkstra(v1_index)[v]
    min_val = min(one,two)

    if min_val < float('inf'):
        print(min(one,two))
    else:
        print(-1)



    
if __name__ == '__main__':
    main()

