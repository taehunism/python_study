# a = [1,2,3,4,5,6,7,8,9,10]
# for v in a:
#     print(v)
    
# b = (1,2,3,4,5,6,7,8,9,10)
# for v in b:
#     print(v)

# c= '안녕하세요'
# for v in c:
#     print(v)

# help(range)

# for v in range(10,15):
#     print(v)
    
# for v in range(0,15,2):
#     print(v)
    
# break는 반복문을 멈추고 밖으로 나가는 것
# continue는 반복문을 멈추고 다음 반복문 step으로 넘어감

for i in range(10):
    if(i==5): 
        #print('으앗 탈출')
        #break
        print('으앗 다음~')
        continue
    print(i)
    i += 1
    
    
# while은 반복 횟수가 정해져있지 않은 경우
# for는 반복 횟수가 정해져 있는 경우 많이 사용