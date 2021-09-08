import sys

def main():
    # n개의 자료형을 받아와서 -> n: 두번째줄에서 입력받을 자료의 길이
    # k : 앞에서 k번째 자료형을 가져오기위한 인덱스값,
    # i : 뒤에서 i번째 자료형을 가져오기위한 인덱스값,
    n,k,i = map(int,sys.stdin.readline().split())
    # 입력받은 줄을 공백을 기준으로 나누어주고 int로 자료형을 정해주어서 n,k,i의 값을 각각 할당해준다음
    input_arr = list(map(int,sys.stdin.readline().split()))
    # 첫번째 줄에서 한 기능과 같되 입력받은 줄을 공백 기준으로 나누어준후 배열의 형태로 저장해서 
    # k, i 를 이용해 해당 위치의 자료를 가져온다.
    # python내부의 정렬기능을 사용해 작은값부터 정렬한다음 -> 몇번째순서인지파악하기위함
    input_arr.sort()
    # 문제에서 요구한 위치에 맞는 두개의 값을 더해서 출력해준다
    print(input_arr[k-1]+input_arr[n-i])
    
if __name__ == '__main__':
    main()
