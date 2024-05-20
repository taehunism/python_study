# pickle은 데이터를 파일로 저장하는 방법
# open()과 다른점이 있음. open은 텍스트 형태로 저장되지만 데이터 구조는 사용하지 않음
# pickle은 bnary 형태로 저장하게 되어, 불러 왔을 때 원본 그대로 사용 가능

#저장 시
# open()
# 쓰기 모드로 열고, dump() 함수 호출
#로드 시
# open()
# 읽기 모드로 열고, load() 함수 호출

class TestClass:
    def __init__(self, text):
        self.text = text
    def print(self):
        print(self.text)

test = TestClass('테스트')
test.print()

import pickle

with open('test.pkl','wb') as f:
    pickle.dump(test, f)
    
with open('test.pkl', 'rb') as f:
    test2 = pickle.load(f)
    
print(type(test2))
test2.print()