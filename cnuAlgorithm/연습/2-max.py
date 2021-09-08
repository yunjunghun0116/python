import random
import time
import matplotlib.pyplot as plt

def main():
    SortimeTimes = []
    FindTimes = []
    for listSize in range(100000,1000000,200000):
        alist = [random.randrange(1000) for x in range(listSize)]
        start = time.time()
        find_max(alist)
        end = time.time()
        runTime = end - start
        FindTimes.append(runTime)

        start = time.time()
        find_max_sorting(alist)
        end = time.time()
        runTime = end - start
        SortimeTimes.append(runTime)

    sizes = range(100000,1000000,200000)
    plt.figure(figsize=(8,5))
    plt.plot(sizes, SortimeTimes,marker='x',c='r',label='findMaxTimeSorting'),
    plt.plot(sizes, FindTimes,marker='x',c='g',label='findMaxTime'),
    plt.xlabel('Input size')
    plt.ylabel('Time (second)')
    plt.legend(loc = 2)
    plt.grid()
    plt.title('Complexity')
    plt.savefig('complexity.png',bbox_inches='tight')





def find_max(input_list):
    temp_max = input_list[0]
    for i in input_list:
        if i > temp_max:
            temp_max = i
    return temp_max

def find_max_sorting(input_list):
    input_list.sort()
    return input_list[-1]
    

if __name__ == '__main__':
    main()

