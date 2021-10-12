import sys

def find(n_list:list,val:int):
    list_len = len(n_list)
    if list_len == 0:
        return False

    mid = (list_len-1)//2
    if n_list[mid] == val:
        return True

    if n_list[mid] < val:
        return find(n_list[mid+1:],val)
    else:
        return find(n_list[:mid],val)

def solve(n_list:list,m_list:list):
    n_list.sort()
    for i in range(len(m_list)):
        if find(n_list,m_list[i]):
            print(1)
        else:
            print(0)

    

def main():
    n_size = int(sys.stdin.readline().strip())
    n_list = list(map(int,sys.stdin.readline().strip().split()))
    m_size = int(sys.stdin.readline().strip())
    m_list = list(map(int,sys.stdin.readline().strip().split()))
    result = solve(n_list,m_list)
if __name__ == '__main__':
    main()
