import sys

def main():
    n = sys.stdin.readline()
    n_data = set(sys.stdin.readline().split())
    m = int(sys.stdin.readline())
    m_data = sys.stdin.readline().split()
    for i in range(m):
        if m_data[i] in n_data:
            print(1)
        else:
            print(0)

    
if __name__ == '__main__':
    main()

