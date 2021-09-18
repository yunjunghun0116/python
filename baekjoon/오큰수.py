import sys

def main():
    size = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    # 배열을 -1로 일단 초기화 시킨다.
    result = [-1 for _ in range(size)]
    stack = [] # 이 스택에 들어갈 원소는 모두 현재 오큰수를 찾지못한 원소만 들어간다.
    for i in range(size):
        if len(stack) == 0:
            stack.append(i)
        else:
            while len(stack) != 0:
                #if stack에 data가 남아있으면 peek(맨 뒤의 원소)를 보고 만약
                #지금 순서의 데이터보다(nums[i]보다) 작으면 맨뒤의 원소의 오른쪽에있으면서
                #큰 값인 오큰수를 찾은것이기 때문에 해당 인덱스의 result를 nums[i]로
                #바꾸어 준다.
                #그리고 오큰수를 찾았으니 뽑아준다.
                if nums[i] > nums[stack[-1]] :
                    result[stack[-1]] = nums[i]
                    stack.pop()
                else:
                    break
            stack.append(i)
    
    
    print(' '.join([str(_) for _ in result]))

    

if __name__ == '__main__':
    main()

