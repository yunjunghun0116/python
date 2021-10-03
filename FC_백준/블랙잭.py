import sys

def find(nums,curr_nums,size,result):
    if len(curr_nums) == size:
        append_num = curr_nums[:]
        result.append(append_num)
    else:
        for i in range(len(nums)):
            if nums[i] in curr_nums :
                continue
            if len(curr_nums) != 0:
                if nums[i] < curr_nums[-1]:
                    continue
            
            curr_nums.append(nums[i])
            find(nums,curr_nums,size,result)
            curr_nums.pop()
def find_sum(nums,m):
    sum_max = 0
    for i in range(len(nums)):
        sum_i = sum(nums[i])
        if sum_i > m:
            continue
        sum_max = max(sum_max,sum_i)
    return sum_max

def main():
    n,m = map(int,sys.stdin.readline().split())
    nums = list(map(int,sys.stdin.readline().split()))
    result = []
    find(nums,[],3,result)
    print(find_sum(result,m))

    

    

if __name__ == '__main__':
    main()

