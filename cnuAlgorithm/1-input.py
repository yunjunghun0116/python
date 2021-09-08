import sys

def main():
    #수 입력받아온후
    n,k,i = map(int,sys.stdin.readline().split())
    #이후 받아오는 모든 수들을 배열로 정리한다음에
    input_arr = list(map(int,sys.stdin.readline().split()))
    #파이썬 내부 정렬기능 사용후
    input_arr.sort()
    #해당 위치 출력
    print(input_arr[k-1]+input_arr[n-i])



if __name__ == '__main__':
    main()

