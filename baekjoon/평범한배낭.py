import sys

def main():
    n,k = map(int,sys.stdin.readline().split())
    dp = [[0 for _ in range(k+1)]for _ in range(n+1)]
    #weight가 0일때는 고려할 필요자체가 없기때문에 1부터 시작해줌
    for i in range(1,n+1):
        weight,value = map(int,sys.stdin.readline().split())
        for j in range(1,k+1):
            if j < weight:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-weight]+value)


    print(dp[n][k])


    

if __name__ == '__main__':
    main()

