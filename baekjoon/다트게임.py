import sys

def solution(dartResult):
    result = []
    current_idx = -1
    data = list(map(str,dartResult))
    if '\n' in data:
        data.remove('\n')
    start = 0
    while start != len(data):
        if data[start].isdigit():
            if data[start] == '1':
                current_idx+=1
                if data[start+1] == '0':
                    result.append(10)
                    start+=1
                else:
                    result.append(int(data[start]))
            else:
                current_idx+=1
                result.append(int(data[start]))
        else:
            if data[start] == 'S':
                result[current_idx] = result[current_idx]
            elif data[start] == 'D':
                result[current_idx] = result[current_idx]**2
            elif data[start] == 'T':
                result[current_idx] = result[current_idx]**3
            elif data[start] == '*':
                if current_idx == 0:
                    result[current_idx] = result[current_idx] * 2
                else:
                    result[current_idx-1] = result[current_idx-1]* 2
                    result[current_idx] = result[current_idx]* 2
            else:
                result[current_idx] = result[current_idx] * (-1)
        start+=1
    return sum(result)

def main():
    input_data = sys.stdin.readline()
    print(solution(input_data))
        
    

if __name__ == '__main__':
    main()

