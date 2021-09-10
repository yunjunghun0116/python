# 동적계획법(DP) 분할정복(DevideConquer)의 공통점
# 문제를 잘게 쪼개서 가장 작은 단위로 분할한 후에 해결한다.
# 차이점
# 동적계획법 : 부분문제는 중복되어 상위문제해결시 결과가 재활용된다. ex) 피보나치수열
#           부분 문제의 해답을 저장한 후에 재활용하는 최적화 기법
# 분할정복 :  부분 문제는 서로 중복되지 않고
#           메모이제이션 기법을 사용하지 않는다.
# 더이상 나눌수 없을때까지 잘게 쪼갠후에 다시 합병하며 문제의 답을 얻는 알고리즘 -> 재귀를 주로이용
# 병합정렬 퀵정렬이 대표 예시

# DP : n == 0 : 0, n == 1 : 1, n == 2: 1임을 이용해서 결과를 저장해놓고 이 결과값을 이용해 피보나치수열의 값을
#      구하는것과 같다.


# 재귀용법을 사용한 피보나치
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
# DP를 이용한 피보나치
def fibonacci_dp(n):
    # 0~n까지 가지고 있는 배열
    # 배열을 초기화해준다
    cache = [0 for index in range(n+1)]
    cache[0] = 0
    cache[1] = 1
    for i in range(2,n+1):
        cache[i] = cache[i-1]+cache[i-2]
    return cache[n]


print(fibonacci(7))
print(fibonacci_dp(7))