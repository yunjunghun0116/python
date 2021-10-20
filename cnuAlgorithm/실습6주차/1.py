import sys
from collections import defaultdict
def bfs(graph,start):
    result = []
    my_queue = []
    result.append(start) # 맨 첫번째 key을 넣어주고
    my_queue.extend(graph[start]) # 해당 key의 values, 즉 graph에 있는 원소들을 하나하나 나누어서 삽입해준다.
    while my_queue:
        # my_queue라는 배열이 빌때까지 계속 맨 첫번째에서 원소를 꺼내고 탐색(bfs)를 진행한다.
        value = my_queue.pop(0)
        if value not in result:
            result.append(value)
            my_queue.extend(graph[value])
    return result

def dfs(graph,start):
    result = []
    my_stack = []
    result.append(start) # 맨 첫번째 key을 넣어주고
    my_stack.extend(graph[start]) # 해당 key의 values, 즉 graph에 있는 원소들을 하나하나 나누어서 삽입해준다.
    while my_stack:
        # stack이라는 배열의 맨 마지막에서 하나씩 빼가면서 탐색을 진행한다.
        value = my_stack.pop()
        if value not in result:
            result.append(value)
            my_stack.extend(graph[value])
    return result

def main():
    start = sys.stdin.readline().strip()
    graphs = defaultdict(list)
    for _ in range(12):
        input = list(map(str,sys.stdin.readline().strip().split()))
        key = input[0] # dictionary에 저장하기위한 key값을 받는다.
        values = input[1:] # dictionary에 저장하기위한 value를 리스트형식으로 받는다.
        graphs[key].extend(values)
    print(*bfs(graphs,start))
    print(*dfs(graphs,start))

if __name__ == '__main__':
    main()