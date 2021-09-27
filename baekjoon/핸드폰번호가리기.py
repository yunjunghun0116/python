import sys

def main():
    number = list(map(str,sys.stdin.readline()))
    find = 0
    length = len(number)
    for i in range(length):
        if number[i] == '-' or number[i] == '\n':
            number[i] = 'check'
            find+=1
    nums_str = ''
    size = 0
    for i in range(length):
        if number[i] != 'check':
            if size < length - find-4:
                nums_str = nums_str +'*'
            else:
                nums_str = nums_str +str(number[i])
            size+=1
        
    print(nums_str)
    
    
    
    
    

    
if __name__ == '__main__':
    main()

