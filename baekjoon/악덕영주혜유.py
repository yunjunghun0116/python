import sys

def main():
    n,k = map(int,sys.stdin.readline().split())

    edges = []
    parent = [i for i in range(n)]
    for _ in range(k):
        start,end,value = map(int,sys.stdin.readline().split())
        edges.append((value,start,end))

    def find_parent(x):
        if parent[x] != x:
            return find_parent(parent[x])
        return parent[x]

    def union(start,end):
        root_start = find_parent(start)
        root_end = find_parent(end)
        if root_start < root_end:
            parent[root_end] = root_start
        else:
            parent[root_start] = root_end

    edges.sort()
    mst = []
    links = []
    for edge in edges:
        value,start,end = edge
        if find_parent(start) != find_parent(end):
            union(start,end)
            mst.append(value)
            links.append((start,end,value))

    board = [[0 for _ in range(n)]for _ in range(n)]
    for link in links:
        start,end,value = link
        board[start][end] = value
        board[end][start] = value

    #dfs 문제
    def dfs(start):
        stack = []
        result = [0 for i in range(n)]
        visited = [0 for _ in range(n)]
        stack.append((0,start))
        ds_max = 0

        while len(stack) != 0:
            value,index = stack.pop()
            for i in range(n):
                if board[index][i] == 0:
                    continue
                elif i ==start :
                    continue
                elif visited[i] == 0:
                    if board[index][i] + value >= result[i]:
                        new_val = board[index][i] + value
                        result[i] =new_val
                        ds_max = new_val
                        stack.append((new_val,i))
                        visited[i] = 1
            
        return ds_max
    dist_max = 0
    for i in range(n):
        dist_max = max(dist_max,dfs(i))
    print(sum(mst))
    print(int(dist_max))

    

if __name__ == '__main__':
    main()

