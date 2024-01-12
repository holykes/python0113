'''
print()
'''
print(10)
print("hello")
print(1+2+3+4)
print("hello "+"python")
print()
print('a','c','e')

# sep 옵션
print(10,20,30,sep='/')
print('a','c','e',sep='-')

# end 옵션
print("hello",end='')
print(1+2+3+4,end=':::')
print("python")

# multi line
print("동해물과 백두산이 마르고 닳도록")
print("대한사람 대한으로 우리나라 만세.")

# 행 끝에 오는 백슬래시는 줄바꿈 무시하라는 뜻
print('''\
동해물과 백두산이 마르고 닳도록
	대한사람 대한으로 우리나라 만세.\
''')

# escape character : 특별한 기능을 수행하도록 정의된 문자로 백슬래시(\)와 함께 사용되는 문자
'''
  \와 조합된 특별한 기능을 수행하는 문자
  \n: 줄 바꿈
  \t: 탭
  \b: 백스페이스
  \\: \
  \': '
  \":"
'''
print("동해물과\n백두산이\t마르고 닳도록")
print("I\'m Elsa")
print("I'm Elsa")


# raw string : escape 문자로 해석되지 않게 설정.
file_path="c:\test\imgs\cat.png"   # \t
print(file_path)

file_path=r"c:\test\imgs\cat.png"
print(file_path)



