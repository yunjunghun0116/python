import sys

def main():
    cnt = int(sys.stdin.readline())
    result = []
    def find(length):
        if length == 1:
            return 1
        elif length == 2:
            return 2
        else:
            res = int(length**(1/2))
            if length == res*res:
                return 2*res-1
            else:
                if length >res*res+res:
                    return 2*res+1
                else:
                    return 2*res
    for _ in range(cnt):
        x,y = map(int,sys.stdin.readline().split())
        length = y-x
        result.append(find(length))
    for i in range(cnt):
        print(result[i])
    

    

if __name__ == '__main__':
    main()

