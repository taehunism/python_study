#패키지란?
#모듈을 관리하기 위한 폴더(디렉토리)
# 상위폴더 - 하위폴더 - 모듈 구조

#패키지 사용방법 import 패키지명.모듈명
# .(dot)으로 패키지안에 모듈에 접근할 수 있음

# as는 별명 지어주는거임 -> alias
import packageTest1.module1 as p1
import packageTest2.module2 as p2

p1.test()
p2.test()

from packageTest1 import module1
module1.test()

from packageTest2 import module2 as m2
m2.test() 
