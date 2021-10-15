import sys

def solve(lines,need):
    left = 1
    right = max(lines)
    while left<=right:
        mid = (left+right)//2
        curr_cnt = 0
        for i in lines:
            curr_cnt += i//mid
        if curr_cnt >= need:
            left = mid+1
            result = mid
        else:
            right = mid-1
    return result



def main():
    cnt,need = map(int,sys.stdin.readline().strip().split())
    lines = []
    for i in range(cnt):
        lines.append(int(sys.stdin.readline().strip()))
    print(solve(lines,need))

if __name__ == '__main__':
    main()
