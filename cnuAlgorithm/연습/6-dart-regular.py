import re
import sys

def calc_dart(input_string):
    # p = re.compile('(\d+)([a-zA-Z\)(\*|#)?')
    # \d의 의미는 숫자를 의미.\D는 문자를 의미(한글 영문 공백 특수기호등)
    # \w의 의미는 워드를 의미
    # \s는 공백을 의미
    p = re.compile('(\d+)([a-zA-Z])([*#]?)')
    score_list = p.findall(input_string)
    result = []
    for i,score in enumerate(score_list):
        print(score)
        point = score[0]
        bonus = score[1]
        option = score[2]
        if bonus == 'S' : bonus = 1
        elif bonus == 'D' : bonus = 2
        elif bonus == 'T' : bonus = 3
        if option == '*':
            if i == 0:
                result.append(int(point)**bonus*2)
            else:
                result[-1] *= 2
                result.append(int(point)**bonus*2)
        elif option == '#':
            result.append(int(point)**bonus*-1)
        else:
            result.append(int(point)**bonus)
    return sum(result)
def main():
    input_string = str(sys.stdin.readline())
    input_string.replace('\n','')
    print(calc_dart(input_string))


if __name__ == '__main__':
    main()
