import sys

def ucleed(n,m):
    max_num = max(n,m) # 큰수를 저장해줄 변수를 선언
    min_num = min(n,m) # 작은수를 저장해줄 변수 선언
    temp = 0
    while max_num % min_num != 0:
        temp = max_num % min_num # 새로운 제수를 저장해주기 위한 서브변수temp 선언
        max_num = min_num
        min_num = temp
    return min_num # 나머지가 0일경우 while문을 탈출하니까 이경우에 새로운 제수를 저장
    

def main():
    n,m = map(int,sys.stdin.readline().split())
    print(ucleed(n,m))

    
if __name__ == '__main__':
    main()
