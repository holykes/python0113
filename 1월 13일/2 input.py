'''
input()
   input()함수는 입력값을 무조건 문자열로 저장한다
'''
# prompt가 없는 경우
name = input()
print(name + "님! 환영합니다.")

# prompt가 있는 경우
name = input("이름을 입력하세요: ")
print(name + "님! 환영합니다.")

# 나이 계산 (오류 발생)
age = input("나이를 입력하세요: ")
print(age - 1)

# 나이 계산 (오류 수정)
age = int(input("나이를 입력하세요: "))
# age = float(input("나이를 입력하세요: "))
print(age - 1)




