'''
변수 : 데이터를 저장할 때 사용하는 메모리 공간.
변수 선언과 할당
	변수명=값   
'''
# 변수 선언
a = 10
b = "hello"
c = 10
print(a, b, c)

# 변수의 주소 확인(객체의 주소) : id()
print(a, "의 주소:", id(a))
print(b, "의 주소:", id(b))
print(c, "의 주소:", id(c))

# 변수 재정의 후 변수의 주소 확인
c = 30
print(id(c))

# 동시 선언
a, b, c = 1, 3.4, "hi"

# 동일한 값을 여러 변수에 할당
a = b = c = "good"
print(id(a))
print(id(b))
print(id(c))


# 변수명 작성 규칙
'''
영문, 한글, 숫자, 밑줄(_)를 사용한다.
변수명은 반드시 문자나 밑줄로 시작한다.
특수문자나 공백 사용 불가.
알파벳은 대소문자를 구분.
파이썬의 예약어는 사용 불가.
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
# 파이썬 예약어 확인
from keyword import kwlist

print(kwlist)

# 변수명 표기 방식
'''
camel case	: userName
snake case	: user_name, 파이썬의 기본 표기 방식(변수명, 함수명)
pascal case	: UserName, 클래스명
'''
# PEP 8 Style Details
'''
https://peps.python.org/pep-0008/
- 변수 및 함수명은 스네이크케이스(Snake_Case)로 작성한다. 
- 클래스명은 카멜케이스(CamelCase)로 작성한다.

코드 레이아웃과 공백
- 들여쓰기는 공백 4칸을 권장한다.
- 한 줄은 최대 79자까지 작성한다.
- 최상위 함수와 클래스 정의는 2줄씩 띄어 쓴다.
- 클래스 내 매소드 정의는 1줄씩 띄어 쓴다.
- 불필요한 공백은 피한다. (대괄호와 소괄호 안 / 쉼표와 쌍점과 쌍반점 앞)
- 키워드 인자와 인자의 기본값의 =는 붙여 쓴다.
- 변수 할당 앞 뒤에 스페이스 공백을 하나 사용한다
'''
