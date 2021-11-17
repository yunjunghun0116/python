import sys
from collections import defaultdict

def main():
    tree = defaultdict(list)
    cnt = int(sys.stdin.readline().strip())
    m,n = map(str,sys.stdin.readline().strip().split()) #m,n의 최소공통조상을찾으면된다.
    si_list = list(map(str,sys.stdin.readline().strip().split()))
    for i in range(1,cnt):
        parent,child = si_list[0],si_list[i]
        tree[parent].append(child)
        tree[child].append(parent)
    for _ in range(cnt-1):
        gu_list = list(map(str,sys.stdin.readline().strip().split()))
        for i in range(1,len(gu_list)):
            parent,child = gu_list[0],gu_list[i]
            tree[parent].append(child)
            tree[child].append(parent)
    
    tree_keys = tree.keys()  
    if(m not in tree_keys or n not in tree_keys):#이상한 값이 입력되는경우 0을 출력
        print(0)
    elif(m == n): # 같을경우 같은값을 출력해준다.
        print(m)
    elif(m == tree[n][0]): # 우측값의 부모노드가 자기자신일경우
        print(m)
    elif(n == tree[m][0]): # 좌측값의 부모노드가 자기자신일경우
        print(n)
    elif(tree[m][0] == tree[n][0]): # 부모가 서로 같을경우
        print(tree[m][0])
    elif(tree[m][0] not in tree_keys or tree[n][0] not in tree_keys):
        print(0)
    elif(tree[tree[m][0]][0] == tree[tree[n][0]][0]): #부모는 다르나 다른부모의 부모(국가) 가 같을경우
        print(tree[tree[m][0]][0])
    else:
        print(0)


if __name__ == '__main__':
    main()
