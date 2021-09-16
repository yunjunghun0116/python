import sys

def main():
    size = int(sys.stdin.readline())
    dp = [0 for _ in range(size+1)]
    for i in range(1,size+1):
        if i == 1:
            dp[i] = 0
        elif i == 2:
            dp[i] = 1
        elif i == 3:
            dp[i] = 1
        else:
            if i%2 == 0 and i%3 == 0:
                dp[i] = min(dp[i//2],dp[i//3],dp[i-1])+1
            elif i%2 ==0:
                dp[i] = min(dp[i//2],dp[i-1])+1
            elif i%3 ==0:
                dp[i] = min(dp[i//3],dp[i-1])+1
            else:
                dp[i] = dp[i-1]+1

    print(dp[-1])

    

if __name__ == '__main__':
    main()

