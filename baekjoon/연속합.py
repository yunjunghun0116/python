import sys

def main():
    
    size = int(sys.stdin.readline())
    nums = list(map(int,sys.stdin.readline().split()))
    result = [0 for i in range(size)]
    for i in range(size):
        if i == 0:
            result[i] = nums[i]
        result[i] = max(nums[i],result[i-1]+nums[i])
    print(max(result))

    
if __name__ == '__main__':
    main()

