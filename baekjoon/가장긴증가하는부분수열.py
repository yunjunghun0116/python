import sys

def main():
    size = int(sys.stdin.readline())
    dp = list(map(int,sys.stdin.readline().split()))
    dist = [1 for _ in range(size)]

    for i in range(1,size):
        dist_max = dist[i]
        index = i-1
        while index >= 0:
            if dp[index] < dp[i]:
                if dist[index]+dist[i] > dist_max:
                    dist_max = dist[index]+dist[i]
            index -=1
            
    
        dist[i] = dist_max
    
             
    print(max(dist))

    

if __name__ == '__main__':
    main()

