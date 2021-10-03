import sys

def up_lines(lines):
    dp = [1 for _ in range(len(lines))]
    for i in range(1,len(lines)):
        for j in range(i):
            if lines[j] <= lines[i]:
                dp[i] = max(dp[j]+1,dp[i])
    return max(dp)

def main():
    n = int(sys.stdin.readline())
    lines = []
    end_lines = []
    for _ in range(n):
        start,end = map(int,sys.stdin.readline().split())
        lines.append((start,end))
    lines.sort()
    for i in range(n):
        end_lines.append(lines[i][1])
    cnt_max = up_lines(end_lines)
    print(n - cnt_max)

if __name__ == '__main__':
    main()

