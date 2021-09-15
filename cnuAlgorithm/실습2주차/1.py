import sys

def fibonacci(n):
    # n에 따라 리턴값이 달라지도록
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        # 예외값처리해줄필요없을경우 재귀를 통해 호출진행한다.
        return fibonacci(n-1)+fibonacci(n-2)

def main():
    n = int(sys.stdin.readline())
    print(fibonacci(n))

    
if __name__ == '__main__':
    main()
