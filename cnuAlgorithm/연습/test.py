def main():
    for i in range(5):
        #1부터 시작할것이기때문에
        startNum = i + 1
        #최대길이의 배열을 생성한 후에 배열의 각 원소를 0으로 초기화시켜줌
        printarr = [0 for i in range(9)]
        #여기서부턴 위치에 숫자를 넣는과정
        for j in range(4-i,5+i):
            if j < 4:
                printarr[j] = startNum
                startNum+=1
            else :
                printarr[j] = startNum
                startNum-=1

        #여기서부턴 출력하기위한 과정이라서 다를수도있음
        printres = ""
        for a in range(9):
            if printarr[a] != 0:
                printres = printres + str(printarr[a])
            else:
                printres = printres + " "
        print(printres)


if __name__ == '__main__':
    main()

