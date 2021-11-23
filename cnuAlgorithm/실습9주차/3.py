import sys
    
def main():
    cnt = int(sys.stdin.readline().strip())
    input_list = list(map(int,sys.stdin.readline().strip().split()))
    target = float(sys.stdin.readline().strip())
    target_cnt = int(sys.stdin.readline().strip())
    # target과 차이가 적은값이 결국 원하는 값이기때문에 해당 값을기준으로 정렬을 진행한후에
    result = sorted(input_list, key=lambda x: (abs(x-target),x))
    
    output_str = ""
    for i in range(target_cnt):
        # 필요한만큼만 떼내서 문자화한후 제출한다.
        output_str += str(result[i]) + " "
        
    print(output_str)  
        

if __name__ == '__main__':
    main()
