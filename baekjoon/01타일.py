import sys

def main():
    size = int(sys.stdin.readline())
    dp = [0 for _ in range(size+1)]
    if size == 1:
        dp[size]=1
    else :
        dp[1] = 1
        dp[2] = 2
    for i in range(3,size+1):
        dp[i] = (dp[i-1]+dp[i-2])%15746
    
    print(dp[-1])


if __name__ == '__main__':
    main()

