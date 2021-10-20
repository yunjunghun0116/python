import sys
from collections import defaultdict

def firstCnt(graph):
    cnt = 0
    keys = []
    keys.extend(graph.keys())
    visited = []
    stack = []
    def dfs(i):
        start = keys[i]
        visited.append(start)
        stack.extend(graph[start])
        while stack:
            val = stack.pop()
            if val not in visited:
                visited.append(val)
                stack.extend(graph[val])
    for i in range(len(keys)):
        if keys[i] not in visited:
            dfs(i)
            cnt+=1

    return cnt

def check(graph_cnt,temp_graph):
    cnt = 0
    keys = []
    keys.extend(temp_graph.keys())
    visited = []
    stack = []
    def dfs(i):
        start = keys[i]
        visited.append(start)
        stack.extend(temp_graph[start])
        while stack:
            val = stack.pop()
            if val not in visited:
                visited.append(val)
                stack.extend(temp_graph[val])
    for i in range(len(keys)):
        if keys[i] not in visited:
            dfs(i)
            cnt+=1

    if graph_cnt == cnt:
        return False
    else: 
        return True

def find(graph):
    firstCount = firstCnt(graph)
    result = []
    temp_graph = graph.copy()
    for key in graph:
        length = len(graph[key])
        for i in range(length):
            val = temp_graph[key][i]
            temp_index = temp_graph[val].index(key)
            temp_graph[key].pop(i)
            temp_graph[val].pop(temp_index)
            if check(firstCount,temp_graph):
                result.append((key,val))
            temp_graph[key].insert(i,val)
            temp_graph[val].insert(temp_index,key)

    return result
    

    

def main():
    cities,cnt = map(int,sys.stdin.readline().strip().split())
    graph = defaultdict(list)
    for _ in range(cnt):
        start,end = map(int,sys.stdin.readline().strip().split())
        graph[start].append(end)
        graph[end].append(start)

    results = defaultdict(list)
    result = find(graph)
    for i in range(len(result)):
        start,end = result[i]
        if start > end:
            if start not in results[end]:
                results[end].append(start)
        else:
            if end not in results[start]:
                results[start].append(end)

    output_result = []
    for key in results:
        for i in range(len(results[key])):
            output_result.append((key,results[key][i]))
    output_result.sort()
    for i in range(len(output_result)):
        start,end = output_result[i]
        print(start,end)



if __name__ == '__main__':
    main()