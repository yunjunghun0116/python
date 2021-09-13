def perm(list):
    length = len(list)
    if length == 1:
        return [list]
    else:
        result = []
        for i in list:
            temp = list.copy()
            temp.remove(i)
            for j in perm(temp):
                j.insert(0,i)
                if j not in result:
                    result.append(j)

    return result
def permutation(list):
    length = len(list)
    if length == 1:
        return [list]
    else:
        nowdata = []
        dfs(list,nowdata)


def dfs(list,nowdata):
    length = len(list)
    if len(nowdata) == length:
        print(nowdata)
        return
    else:
        for i in range(1,length+1):
            if i in nowdata:
                continue
            else:
                dfs(list,nowdata+[i])



def main():
    n = int(input())
    input_arr = [i for i in range(1,n+1)]
    permutation(input_arr)


if __name__ == '__main__':
    main()

