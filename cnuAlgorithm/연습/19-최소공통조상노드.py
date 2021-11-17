from collections import deque
import sys
import math

def generate_tree(tree,n):
    for _ in range(n-1):
        parent,child = map(str,sys.stdin.readline().strip().split())
        tree[child].append(parent) #dfs 실행시 child로 돌아가는 연산 필요
        tree[parent].append(child)
def dfs(tree,parent_list,depth,n):
    visited = [False for _ in range(n+1)]
    q = deque()
    q.append(1)
    while q:
        p = q.popleft()
        visited[p] = True
        for i in tree[p]:    
            if visited[i] == False:
                q.append(i)
                parent_list[i] = p
                depth[i] = depth[p]+1
                
def compute_exp_parent(exp_parent,n):
    logn = int(math.log2(n)+1)
    for i in range(1,n+1):
        for j in range(1,logn):
            exp_parent[i][j] = exp_parent[exp_parent[i][j-1]][j-1]
                
def search_lca(exp_parent,depth,n,m):
    logn = int(math.log2(n)+1)
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().strip().split())
        if(depth[a]>depth[b]):
            a,b = b,a
        level_diff = depth[b]-depth[a]
        for i in range(logn):
            if level_diff & 1 << i:
                b = exp_parent[b][i]
        if a == b:
            print(a)
            continue
        
        for i in range(logn -1,-1,-1):
            if exp_parent[a][i] != exp_parent[b][i]:
                a = exp_parent[a][i]
                b = exp_parent[b][i]
        print(exp_parent[b][0])
                
def main():
    n = int(sys.stdin.readline().strip())
    tree = [[] for _ in range(n+1)]
    
    generate_tree(tree,n) # tree를 만든다
    
    parent_list = [0 for _ in range(n+1)]
    depth = [0 for _ in range(n+1)]
    dfs(tree,parent_list,depth,n) # 트리 노드의 paren를 찾고, 찾으면서 depth도 tree로부터 구하기 위함
    
    logn = (int)(math.log2(n)+1)
    exp_parent = [[0 for _ in range(logn)]for _ in range(n+1)]
    
    for i in range(n+1):
        exp_parent[i][0] = parent_list[i]
    compute_exp_parent(exp_parent,n)
    
    m = int(sys.stdin.readline().strip())
    search_lca(exp_parent,depth,n,m)
        

if __name__ == '__main__':
    main()

# 5
# 1 2
# 1 3
# 2 4
# 2 5
# 2
# 4 3
# 4 5