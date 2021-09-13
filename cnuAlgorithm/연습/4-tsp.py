import itertools

def tsp():
    n = int(input())
    input_list = list(map(int,input().split()))
    src = (input_list[0],input_list[1]) # 출발노드
    dst = (input_list[2],input_list[3]) # 도착노드
    points = []
    points_slice = input_list[4:]

    for i in range(0,len(points_slice),2):
        points.append((points_slice[i],points_slice[i+1]))

    min_distance = float('inf')
    for i in itertools.permutations(points):
        path = [src,*list(i),dst]
        distance = 0
        for j in range(0,len(path)-1):
            distance += abs(path[j][0]-path[j+1][0])+abs(path[j][1]-path[j+1][1])

        min_distance = distance if distance < min_distance else min_distance

    return min_distance

def main():
    test_case = int(input())
    for _ in range(0,test_case):
        print(tsp())




if __name__ == '__main__':
    main()

