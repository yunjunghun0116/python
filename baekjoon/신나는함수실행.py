import sys

def main():
    dp =[[[1 for _ in range(21)]for _ in range(21)]for _ in range(21)]

    for i in range(1,21):
        for j in range(1,21):
            for k in range(1,21):
                if i < j and j < k:
                    dp[i][j][k] = dp[i][j][k-1]+dp[i][j-1][k-1]-dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k]+dp[i-1][j-1][k]+dp[i-1][j][k-1]-dp[i-1][j-1][k-1]

    while True:
        a,b,c = map(int,sys.stdin.readline().split())
        
        if a == -1 and b == -1 and c == -1:
            break
        else:
            if a<=0 or b<=0 or c<= 0:
                result = dp[0][0][0]
            elif a > 20 or b > 20 or c > 20 :
                result = dp[20][20][20]
            elif a < b and b < c:
                result = dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
            else:
                result = dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]
            strs = 'w('+str(a)+', '+str(b)+', '+str(c)+') = '+str(result)
            print(strs)
if __name__ == '__main__':
    main()

