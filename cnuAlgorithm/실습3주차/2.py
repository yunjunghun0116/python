import sys

def solve(s : str):
    #해당 문자열의 길이를 크기로 하는 2차원 배열을 구성하고 False를 준다.
    length = len(s)
    table = [[False for j in range(length)]for i in range(length)]
    #먼저 이 함수는 만약 s[0]과 s[6]이 같으면 s[1]과 s[5]를 비교하고, 안쪽으로 가며 회문인지를
    #파악하는 함수이기때문에 결국 필요한것은 현재 체크하고있는 문자(열이 아닌 해당위치의 문자그자체)
    #가 회문인지 파악하는 함수이다.
    for i in range(length):
        for j in range(length-i):
            # 여기서 i<2를 굳이 빼주는 이유는 기본적으로 자기자신을 체크하는 i == 0일때는 항상
            # 회문이라고 볼 수 있고, s가 1일경우에는 j와 j+1사이에 어떤 문자열이 존재할 수 없기
            #때문에 따로 구분지어준것이고,
            if i < 2:
                if s[j] == s[i+j]:
                    table[j][i+j] = True
                    longest = s[j:i+j+1]
            #위의 조건에서 걸러지지 않았을경우 회문인지 체크하고 맞으면 그 사이
            #table상에서는 왼쪽아래에 해당하는 부분이 True인지 체크하고 만약 맞으면 그 안쪽의 모든
            #문자열이 회문이란 뜻이기때문에 그 문자열자체는 회문이기때문에 해당 길이만큼 문자열을 
            #longest에 저장해준다. 여기서 longest는 이제껏 나온 가장 긴 길이의 회문이다.
            else:
                if s[j] == s[i+j] and table[j+1][i+j-1]:
                    table[j][i+j] = True
                    longest = s[j:i+j+1]
    for i in range(length):
        print(table[i])
    return longest

def main():
    input_str = sys.stdin.readline().strip()
    print(solve(input_str))
    

    
if __name__ == '__main__':
    main()
