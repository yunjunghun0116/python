import sys

def main():
    size = int(sys.stdin.readline())
    dp = list(map(int,sys.stdin.readline().split()))
    dist = [1 for _ in range(size)]
    bitonic = [0 for _ in range(size)]

    for i in range(1,size):
        dist_max = dist[i]
        index = i-1
        while index >= 0:
            if dp[index] < dp[i]:
                if dist[index]+dist[i] > dist_max:
                    dist_max = dist[index]+dist[i]
            index -=1
        dist[i] = dist_max
    for i in range(size):
        up_finish = False
        down_finish = False
        cnt = 0
        while not up_finish and not down_finish:
            index = i
            if not up_finish:
                if dp[i]<dp[i+1]:
                    index+=1
                else:
                    up_finish = not up_finish
            else:
                if dp[i]>dp[i+1]:
                    index+=1
                else:
                    down_finish = not down_finish
            cnt+=1
        bitonic[i] = cnt

    print(max(bitonic))


    

if __name__ == '__main__':
    main()

