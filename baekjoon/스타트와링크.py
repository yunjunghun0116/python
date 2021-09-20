import sys

def main():
    size = int(sys.stdin.readline())
    board = []
    result = []
    for _ in range(size):
        lst = list(map(int,sys.stdin.readline().split()))
        board.append(lst)

    def dfs(currentarr,result,n):
        if len(currentarr) == n//2:
            result.append(currentarr)
        else:
            for i in range(n):
                if i in currentarr:
                    continue
                elif len(currentarr)==0:
                    dfs(currentarr+[i],result,n)
                else:
                    if currentarr[-1]>=i:
                        continue
                    else:
                        dfs(currentarr+[i],result,n)

    def board_sum(arr):
        point_sum = 0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                point_sum += board[arr[i]][arr[j]] + board[arr[j]][arr[i]]
        return point_sum

    def pointDif(arr,n):
        find_arr = [0 for _ in range(n)]
        #find_arr 1:스타트, 0:링크 
        for i in range(len(arr)):
            find_arr[arr[i]] = 1

        start_arr = []
        link_arr = []
        
        for i in range(n):
            if find_arr[i] == 1:
                start_arr.append(i)
            else:
                link_arr.append(i)
        
        start_sum = board_sum(start_arr)
        link_sum = board_sum(link_arr)
        return abs(start_sum-link_sum)

                    
    dfs([],result,size)
    dif_min = float('inf')

    for i in range(len(result)):
        dif_min = min(dif_min,pointDif(result[i],size))
                    
    print(dif_min)






    

if __name__ == '__main__':
    main()

