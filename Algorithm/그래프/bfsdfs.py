# BFS 알고리즘 구현
# 자료구조 Queue를 사용한다
import queue
graph = dict()

graph['a'] = ['b','c']
graph['b'] = ['a','d']
graph['c'] = ['a','g','h','i']
graph['d'] = ['b','e','f']
graph['e'] = ['d']
graph['f'] = ['d']
graph['g'] = ['c']
graph['h'] = ['c']
graph['i'] = ['c','j']
graph['j'] = ['i']



def bfs(graph,start_val):
    bfs_queue = queue.Queue()
    visited = []
    bfs_queue.put(start_val)
    while bfs_queue.qsize() != 0:
        data = bfs_queue.get()
        print(data)
        for i in range(len(graph[data])):
            if visited.__contains__(graph[data][i]):
                continue
            else:
                bfs_queue.put(graph[data][i])
                visited.append(graph[data][i])
        visited.append(start_val)

bfs(graph,'a')

def dfs(graph,start_val):
    visited = []
    

