import sys

def preorder(tree,node,visit_list):
    visit_list.append(node)
    if(tree[node][0] != '.') :
        preorder(tree,tree[node][0],visit_list)
    if(tree[node][1] != '.') :
        preorder(tree,tree[node][1],visit_list)
    
def main():
    n = int(sys.stdin.readline().strip())
    tree = {}
    visit_list = []
    node = None
    for _ in range(n):
        node_list = sys.stdin.readline().strip().split(' ')
        tree[node_list[0]] = [node_list[1],node_list[2]]
        
    preorder(tree,'A',visit_list)

if __name__ == '__main__':
    main()
