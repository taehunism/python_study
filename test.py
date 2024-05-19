# LIST 
# a = [1,2,3,4,5]
# print(type(a))
# print(a[0])
# print(a[4]) # == print(a[-1])
# print(a[0:4]) # 4까지라는 뜻으로, 0 1 2 3 인덱스 출력
# print(a[2:])

a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)

d = a*2 #곱하기는 문자열과 동일한 성질
print(d)

# TUPLE 읽기전용 자료구조라고 생각하면 됨. 추가,삽입,수정,삭제 불가
# 리스트에 비해 처리속도가 빠름
tuple1 = 1,2,3,4,5
tuple2 = (1,2,3,4,5)
print(type(tuple1))
print(type(tuple2))

# 세트
# 중복 허용 X, 순서가 없음(인덱스 X)
a = {1,2,3,4,5}
print(type(a))

a = {1,2,3,1} #중복 못들어옴 
print(a)
a = [1,2,3,1]
b = set(a)
print(b)

# 집합연산
a = {1,2,3}
b = {2,3,4}
print(a.union(b)) #합칩합
print(a.intersection(b)) #교집합
print(a.difference(b)) #차집합

# 딕셔너리
# 자료구조의 중복된 요소 제거 가능, 집합 연산
a = {'name' : '홍길동', 'age':30, 'id':'hong'}
print(type(a))
# 요소 참조
print(a['name'])
print(a['age'])
print(a['id'])
# 요소 추가
a['address'] = '서울'
print(a) 

a['age'] = 40
print(a)

#del(a['address'])
del  a['address']
print(a)
