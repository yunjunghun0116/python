import sys
import re

def solve(s : str):
    #정규표현식으로써 (숫자,SDT세개의 문자중하나,* or # or 공백) 으로 구성된 문자열을
    #구분해서 해당부분만 score_list에 저장을 한 후에 result는 길이가 3이고, 값은 1을 갖고있는
    #상태로 초기화한다.
    p = re.compile('(\d+)([SDT])([*|#]?)')
    score_list = p.findall(s)
    result = [1 for _ in range(3)]
    # -1부터시작하는것은 options를 처리하기위함이다.
    current_index = -1
    for score in score_list:
        current_index += 1
        point,bonus,option = score #튜플의 형태로 꺼낸값을 나누어 저장하고,
        if bonus == 'S' : bonus = 1
        elif bonus == 'D' : bonus = 2
        elif bonus == 'T' : bonus = 3
        if option == '*':
            #조건에 맞게 계산해서 result에 새로 update를 해준다.
            if current_index < 2:
                result[current_index] = result[current_index]*(int(point)**bonus)*2
                #여기서 current_index+1은 무조건 1이기때문에 2로 업데이트해주면 나중에 어떤값을 
                #가공해서 넣어줘도 결국 *2이기때문에 스타상의 효과가 기록된다.
                result[current_index+1] = 2
            else:
                #위에서 걸러지지않은경우는 결국 마지막score이기때문에 자기자신의 점수만 2배한다.
                result[current_index] = result[current_index]*(int(point)**bonus)*2
        elif option == '#':
            result[current_index] = result[current_index]*(int(point)**bonus)*(-1)
        else:
            #여기서는 option이 공백일때만 걸러진것이고, 이때는 score과 bonus로만 점수를 구성해서
            #업데이트 해준다.
            result[current_index] = result[current_index]*(int(point)**bonus)
    return sum(result)


def main():
    input_str = sys.stdin.readline().strip()
    print(solve(input_str))
    

    
if __name__ == '__main__':
    main()
