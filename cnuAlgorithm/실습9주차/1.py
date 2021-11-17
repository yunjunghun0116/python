import sys

def preorder(tree,node,visit_list):
    # 루트를 포함한 후에 
    visit_list.append(node)
    # 왼쪽부터 체크해나간다
    if(tree[node][0] != '.') :
        preorder(tree,tree[node][0],visit_list)
    if(tree[node][1] != '.') :
        preorder(tree,tree[node][1],visit_list)
def inorder(tree,node,visit_list):
    # 왼쪽을 먼저 체크한후에
    if(tree[node][0] != '.') :
        inorder(tree,tree[node][0],visit_list)
    # 자기자신을 확인하고
    visit_list.append(node)
    # 우측 확인한다
    if(tree[node][1] != '.') :
        inorder(tree,tree[node][1],visit_list)
def postorder(tree,node,visit_list):
    # 왼쪽 오른쪽을 모두 확인한 후에
    if(tree[node][0] != '.') :
        postorder(tree,tree[node][0],visit_list)
    if(tree[node][1] != '.') :
        postorder(tree,tree[node][1],visit_list)
    # 자기자신을 확인한다
    visit_list.append(node)
    
def main():
    n = int(sys.stdin.readline().strip())
    tree = {}
    pre_visit_list = []
    in_visit_list = []
    post_visit_list = []
    for _ in range(n):
        node_list = sys.stdin.readline().strip().split(' ')
        tree[node_list[0]] = [node_list[1],node_list[2]]
        
    preorder(tree,'A',pre_visit_list)
    inorder(tree,'A',in_visit_list)
    postorder(tree,'A',post_visit_list)
    print(''.join(pre_visit_list))
    print(''.join(in_visit_list))
    print(''.join(post_visit_list))

if __name__ == '__main__':
    main()