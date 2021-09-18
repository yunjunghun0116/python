import sys

def main():
    n,m = map(int,sys.stdin.readline().split())
    bag_list = []
    bag_weight = []
    for _ in range(n):
        weight,value = map(int,sys.stdin.readline().split())
        bag_list.append((weight,value))
    bag_list = sorted(bag_list,key=lambda x:x[1]/x[0],reverse=True)
    for _ in range(m):
        bag_weight.append(int(sys.stdin.readline()))
    print(bag_list)
    print(bag_weight)

    def greedy(index):
        max_val = 0
        can_size = bag_weight[index]
        for i in range(n):
            if can_size >= bag_list[i][0]:
                can_size -= bag_list[i][0]
                max_val += bag_list[i][1]
        return max_val/bag_weight[index]
    

    
    bag_max = 0
    bag_index = 0
    for i in range(m):
        if bag_max < greedy(i):  
            bag_max = greedy(i)
            bag_index = i
    print(bag_index+1)




    
if __name__ == '__main__':
    main()

