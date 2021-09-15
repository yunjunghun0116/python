import sys



def pyramid(n,size): # n : 4, size : 10
    if size == 1:
        return 1
    else:
        # 기본값인 1 을 저장하기 선언
        nums = [0 for i in range(size+1)]
        for i in range(1,n+1):
            index = i*(i-1)//2+1
            # 1이 들어갈 위치가 아니면 가장먼저 
            # depth가 몇인지를 저장하기위해 i를 저장해준다
            nums[index+1] = i
            nums[index] = 1
            nums[index-1] = 1
        # 배열의 마지막 원소또한 1이지만 위의 for문에서 체크가 안되기때문에
        # 한번 더 진행해준다
        nums[-1] = 1 

        #첫번째 인덱스부터 진행해야하기때문에 start인덱스를 지정해준다.
        start = 0
        while start < size:
            if nums[start] == 1:
                start+=1
            else:
                #여기서 걸리는 경우는 nums[start] = 단계 값을 갖고있다.
                temp = nums[start] # 3단계이기때문에 3을 갖고있음
                # 이후부터 1을 만나기전까지는 0이 저장되어있기때문에 더해준다.
                while nums[start] != 1:
                    nums[start] = nums[start-temp]+nums[start-temp+1]
                    start+=1

        # 모든 단계의 합을 저장하기위한 변수
        _sum = 0
        # 모든 단계의 합을 구하는 함수
        for i in range(1,size+1):
            _sum+=nums[i]


        return _sum
    
def numsSize(n): # 최대 길이를 계산하기 위한 함수
    return n*(n+1)//2

def main():
    n = int(sys.stdin.readline())
    print(pyramid(n,numsSize(n)))

    
if __name__ == '__main__':
    main()
