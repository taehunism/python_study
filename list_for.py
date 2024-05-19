# for i in range(3):
#     for j in range(3):
#         print(f"i = {i}, j= {j}")

# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")        

# a = [1,2,3,4,5,6,7,8,9,10]
# print (a)

# a = [i for i in range(1,11,1)]
# print (a)

# b = []
# for v in a:
#     if v%2 == 0:
#         b.append(v)

# print(b)

import time
start = time.time()
r = []
for v in range(1000000):
    if v%2 == 0:
        r.append(v)
end = time.time()
print(f"포문 소요 시간 : {end - start}")

start = time.time()
r = [v for v in range(1000000) if v%2==0]
# v를 요소로 넣을건데 0부터 1백만 까지 포문을 돌리는데 v가 2로 나눴을 때 나머지가 0일 때만 요소로
end = time.time()
print(f"리스트 포문 소요시간 : {end - start}")