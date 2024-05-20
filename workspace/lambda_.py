#filter
#특정 조건을 만족하는 요소만 남기고 필터링

#map
#순서가 있는 데이터 집합에서 각 욧를 수식에 따라 변형하여 새로운 리스트로 변환
#reduce
#차례대로 앞 2개의 요소를 가지고 연산하며,
#연산의 결과가 또 다음 연산의 입력으로 진행.
#마지막 연산이 끝나면 최종 출력은 한개만 반환(누적 연산)

#filter
# def even(n):
#     return n&2==0
#
# print(even(3))
#
# nums = [i for i in range(1,11)]
# print(nums)
# r = list(filter(even, nums))
# print(r)
#
# r = list(filter(lambda n:n%2==0, nums))
# print(r)

#map
# def pow(n):
#     return n**2
#
# print(pow(3))
#
# nums = [i for i in range(1,11)]
#
# r = []
# for v in nums:
#     r.append(pow(v))
# print(r)
# #함수에 괄호를 넣으면 실행, 없으면 콜백
# r2 = list(map(pow, nums))
# print(r2)
#
# r3 = list(map(lambda n:n**2, nums))
# print(r3)


#reduce

import functools

nums = list(range(1,11))
print(nums)
s=0
for v in nums:
    s += v

print(s)

s2 = functools.reduce(lambda x,y : x+y, nums)
print(s2)

def add(x,y):
    print(f"{x} + {y}")
    return x+y
functools.reduce(add, nums)