import sys
    
def main():
    cnt = int(sys.stdin.readline().strip())
    input_list = list(map(int,sys.stdin.readline().strip().split()))
    target = float(sys.stdin.readline().strip())
    target_cnt = int(sys.stdin.readline().strip())
    result = sorted(input_list, key=lambda x: (abs(x-target),x))
    
    output_str = ""
    for i in range(target_cnt):
        output_str += str(result[i]) + " "
        
    print(output_str)  
        

if __name__ == '__main__':
    main()
