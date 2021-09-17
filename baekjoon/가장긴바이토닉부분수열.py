import sys

def main():
    size = int(sys.stdin.readline())
    dp = list(map(int,sys.stdin.readline().split()))
    up_dist = [1 for _ in range(size)]
    down_dist = [1 for _ in range(size)]

    for i in range(1,size):
        dist_max = up_dist[i]
        index = i-1
        while index >= 0:
            if dp[index] < dp[i]:
                if up_dist[index]+up_dist[i] > dist_max:
                    dist_max = up_dist[index]+up_dist[i]
            index -=1
        up_dist[i] = dist_max

    for i in range(size-2,-1,-1):
        dist_max = down_dist[i]
        index = i+1
        while index <= size-1:
            if dp[index] < dp[i]:
                if down_dist[index]+down_dist[i] > dist_max:
                    dist_max = down_dist[index]+down_dist[i]
            index +=1
        down_dist[i] = dist_max
    dist_max = 0
    for i in range(size):
        dist_max = max(dist_max,up_dist[i]+down_dist[i])

    print(dist_max-1)
    

if __name__ == '__main__':
    main()

