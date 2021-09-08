def main():
    n = int(input()) #입력받은 값을 int자료형으로 형변환해준다음에
    if n%2 == 0: # 짝수 => 2로 나누어지는수이기때문에 처리해주고,
        print('even')
    else : #아닌경우는 홀수로 처리해준다.
        print('odd')
    
if __name__ == '__main__':
    main()