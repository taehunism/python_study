# 예외(exception)
# 오류 : 프로그램 실행 중 오작동이나, 비정상적으로 종료되는 현상
# 예외 : 특정 상황이 발생해서 프로그램이 중단되는 현상(개발자가 해결 가능한 오류)

# try:
#     예외 발생 가능 코드
# except 예외 처리 클래스:
#     예외 발생 시 처리 코드
# finally:
#     예외 발생 여부와 상관없이 실행되는 코드
# except와 finally 구문은 생략 가능

print("program start")
try:
    x=1
    y=0
    print(x/y)
    a = []
    print(a[0])
# except ZeroDivisionError:
#     print("Occured Exception")
# except IndexError:
#     print("index Exception")
except:
    print("exception")
    
finally:
    print("absoultly Exec")
print("program end")