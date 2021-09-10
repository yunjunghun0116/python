#고급정렬알고리즘에서는 재귀용법을 사용함
#재귀호출 -> 스택의 전형적인 예로써 진행된다 == 내부적으로 스택처럼 관리된다
import random

data_list = [];
for i in range(5):
    data_list.append(random.randint(0,999));

def multiple(data):
    if data <= 1:
        return data
    return data*multiple((data-1))

def sum_list(data):
    if len(data) == 1:
        return data[0]
    #현재 배열중 1번의 인덱스부터 끝까지의 합과 data[0]을 합해줌을 리턴해준다
    #배열을 조금씩 줄여나가며 진행하는것
    return data[0]+sum_list(data[1:])

def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        #1:-1 은 0과 -1을 제외한 값을 리턴해주는 기능이다
        return palindrome(string[1:-1])
    else:
        return False

def to_one(n):
    print(int(n))
    if n == 1:
        return 
    else:
        if n%2 == 0:
            return to_one(n/2)
        return to_one(3*n+1)

def one_two_three(n,str):
    if n<=0:
        print(str)
        return 
    if str=="":
        if n == 1:
            one_two_three(n-1,str+"1")
        elif n == 2:
            one_two_three(n-1,str+"1")
            one_two_three(n-2,str+"2")
        else:
            one_two_three(n-1,str+"1")
            one_two_three(n-2,str+"2")
            one_two_three(n-3,str+"3")
    else:
        if n == 1:
            one_two_three(n-1,str+"+1")
        elif n == 2:
            one_two_three(n-1,str+"+1")
            one_two_three(n-2,str+"+2")
        else:
            one_two_three(n-1,str+"+1")
            one_two_three(n-2,str+"+2")
            one_two_three(n-3,str+"+3")
    



print(multiple(10))
print(sum_list(data_list))
print(palindrome("motor"))
to_one(3)
one_two_three(5,"")