import sys

def bfs(graph,start):
    result = []
    my_queue = []
    result.append(start)
    my_queue.extend(graph[start])
    while my_queue:
        value = my_queue.pop(0)
        if value not in result:
            result.append(value)
            my_queue.extend(graph[value])
    return result

def dfs(graph,start):
    result = []
    my_stack = []
    result.append(start)
    my_stack.extend(graph[start])
    while my_stack:
        value = my_stack.pop()
        if value not in result:
            result.append(value)
            my_stack.extend(graph[value])
    return result

def main():
    start = sys.stdin.readline().strip()
    for _ in range(12):
        sys.stdin.readline()
    print()
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H'] 
    }
    print(*bfs(graph,start))
    print(*dfs(graph,start))

    

if __name__ == '__main__':
    main()