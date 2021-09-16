import sys

def main():
    size = int(sys.stdin.readline())
    stair = [0 for _ in range(size+1)]
    dp = [0 for _ in range(size+1)]
    for i in range(size):
        stair[i+1] = int(sys.stdin.readline())
    for i in range(1,size+1):
        if i == 1:
            dp[i] = stair[i]
        elif i == 2 :
            dp[i] = max(dp[i-2],stair[i-1])+stair[i]
        else:
            dp[i] = max(dp[i-2],dp[i-3]+stair[i-1])+stair[i]

    print(dp[-1])


if __name__ == '__main__':
    main()

