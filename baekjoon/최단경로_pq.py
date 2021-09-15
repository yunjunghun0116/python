import sys
from queue import PriorityQueue

def main():
    
    v,e = map(int,sys.stdin.readline().split())
    start = int(sys.stdin.readline())
    board={i : [] for i in range(1,v+1)}
    for _ in range(e):
        start_index,end_index,value = map(int,sys.stdin.readline().split())
        board[start_index].append((end_index,value))

    dist={i : float('inf') for i in range(1,v+1)}
    dist[start] = 0
    my_queue = PriorityQueue()
    my_queue.put((0,start))
   
    while not my_queue.empty():
        cur_dist,cur_index = my_queue.get()
        if cur_dist <= dist[cur_index]:
            for index,value in board[cur_index]:
                if cur_dist + value < dist[index]:
                    dist[index] = cur_dist + value
                    my_queue.put((dist[index],index))

    for dist in dist.values():
        if dist != float('inf'):
            print(dist)
        else:
            print('INF')

    
if __name__ == '__main__':
    main()

