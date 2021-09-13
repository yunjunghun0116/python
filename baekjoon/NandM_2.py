def perm(num,cnt):
    list = [i for i in range(1,num+1)] # 1 2 3 4 5 6 이런식의 배열생성
    result = [] # 결과만족하는것들 담을 그릇
    nowdata = [] # 현재 데이터를 통해 판단하기위한 값
    dfs(list,result,nowdata,cnt)

    return result

def dfs(list,result,nowdata,cnt):
    if len(nowdata) == cnt:
        result.append(nowdata)
    else:
        for i in range(1,len(list)+1):
            if i in nowdata:
                continue
            if nowdata:
                if i < nowdata[-1]:
                    continue
                else:
                    dfs(list,result,nowdata+[i],cnt)
            else:
                dfs(list,result,nowdata+[i],cnt)

    
def main():
    num,cnt = map(int,input().split())
    result = perm(num,cnt)
    for i in range(len(result)):
        string = str(result[i][0])
        for j in range(1,cnt):
           string = string + " "+str(result[i][j])
        print(string)


    
if __name__ == '__main__':
    main()

