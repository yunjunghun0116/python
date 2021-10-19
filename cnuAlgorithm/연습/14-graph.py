import sys

graph = {
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A','F'],
    'D' : ['B'],
    'E' : ['B','F'],
    'F' : ['C','E']
}
def bfs(graph,start_node):
    visit = list()
    queue = list()
    queue.append(start_node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return visit

def dfs(graph,start_node):
    visit = []
    stack = []
    stack.append(start_node)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

def main():
    print(bfs(graph,'A'))
    print(dfs(graph,'A'))
    
if __name__ == '__main__':
    main()

