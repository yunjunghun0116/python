# 0 ~ 999 숫자 중에서 임의로 100개를 추출해서, 이진 탐색 트리에 입력, 검색, 삭제
import random

# 0 ~ 999 중, 100 개의 숫자 랜덤 선택
# set : 중복이 없는 자료구조
nums = set()
while len(nums) != 10:
    nums.add(random.randint(0, 99))

print(nums)
#파이썬의 set에서의 pop기능은 맨처음에 위치한 데이터를 꺼내온다.
print(nums.pop())
print(nums.pop())
print(nums.pop())


