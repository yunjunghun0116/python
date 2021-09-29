import sys
import re

def solve(s : str):
    p = re.compile('(\d+)([SDT])([*|#]?)')
    score_list = p.findall(s)
    result = [1 for _ in range(3)]
    current_index = -1
    for score in score_list:
        current_index += 1
        point,bonus,option = score
        if bonus == 'S' : bonus = 1
        elif bonus == 'D' : bonus = 2
        elif bonus == 'T' : bonus = 3
        if option == '*':
            if current_index < 2:
                result[current_index] = result[current_index]*(int(point)**bonus)*2
                result[current_index+1] = 2
            else:
                result[current_index] = result[current_index]*(int(point)**bonus)*2
        elif option == '#':
            result[current_index] = result[current_index]*(int(point)**bonus)*(-1)
        else:
            result[current_index] = result[current_index]*(int(point)**bonus)
    return sum(result)


def main():
    input_str = sys.stdin.readline().strip()
    print(solve(input_str))
    

    
if __name__ == '__main__':
    main()
