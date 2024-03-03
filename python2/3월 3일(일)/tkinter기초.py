#### 1. 창 만들기 ####
# from tkinter import *
# w=Tk()
#
# w.mainloop()

### 창 아이콘 변경
# from tkinter import *
#
# w = Tk()
# photo=PhotoImage(file='weather.png')
# w.wm_iconphoto(False,photo)
# w.title('날씨 정보 조회')
# w.geometry('300x120')
#
# w.mainloop()

#### 2. 창 크기와 제목 설정 ####
# from tkinter import *
# w=Tk()
# w.title('GUI 프로그래밍')
# w.geometry('300x300')
# w.mainloop()

#### 3. 레이블(Label) 위젯 생성 ####
# from tkinter import *
# w=Tk()
# w.title('GUI 프로그래밍')
# w.geometry('300x300')
# label=Label(w,text='Hi~~~~~')
# label.pack()
# w.mainloop()
#
# label2=Label(w,text='Hi~~~~~',font=('휴먼편지체',20),fg='red')
# label3=Label(w,text='Hi~~~~~',font=('휴먼편지체',20),fg='red',bg='yellow',width=30,height=10,anchor=SE)

### 4.레이블(Label) 위젯에 이미지 넣기.
## ImageTk.PhotoImage()사용
## pip install pillow 설치후 사용
# from tkinter import *
# from PIL import ImageTk
# w=Tk()
# img=ImageTk.PhotoImage(file='wicon.png')
# label1=Label(w,image=img)
# label1.pack()
# w.mainloop()

### 5.버튼(Button) 위젯 생성
# from tkinter import *
# w=Tk()
# w.title('GUI 프로그래밍')
# w.geometry('300x300')
# button=Button(w,text='창 닫기',command=quit)
# button.pack()
#
# w.mainloop()

### 6.버튼 클릭시 "안녕~" 표시하기
# from tkinter import *
# from tkinter import messagebox
# def showHello():
#     messagebox.showinfo('이미지 버튼', '안녕~~')
#
# w = Tk()
# w.title('GUI 프로그래밍')
# w.geometry('300x300')
# button = Button(w,text="인사하기",command=showHello)
# button.pack()
# w.mainloop()

### 7.버튼 클릭시 레이블에 "안녕~" 표시하기
### config(): 위젯의 속성을 설정하거나 수정
# from tkinter import *
# def showHello():
#     label.config(text="안녕^^^^^^")
#     button.config(text="인사 끝!!!")
#
# w = Tk()
# w.title('GUI 프로그래밍')
# w.geometry('300x300')
# button = Button(w,text="인사하기",command=showHello)
# button.pack()
# label=Label(w,text='')
# label.pack()
# w.mainloop()

### 8.텍스트와 엔트리 사용
### Text 위젯 : 여러 줄 입력 가능
### Entry 위젯 : 한 줄만 입력 가능
# from tkinter import *
# w=Tk()
# w.title('GUI 프로그래밍')
# w.geometry('500x200')
# text=Text(w,width=30,height=5)
# text.insert(END,'텍스트를 입력하세요.')
# text.pack()
#
# entry=Entry(w,width=30)
# entry.insert(0,'한 줄만 입력 가능합니다.')
# entry.pack()
#
# w.mainloop()

### 9.버튼 클릭시 텍스트, 엔트리 내용 출력/삭제
# from tkinter import *
# w=Tk()
# w.title('GUI 프로그래밍')
# w.geometry('500x200')
# text=Text(w,width=30,height=5)
# text.insert(END,'텍스트를 입력하세요.')
# text.pack()
#
# entry=Entry(w,width=30)
# entry.insert(0,'한 줄만 입력 가능합니다.')
# entry.pack()
#
# def clean_text():
#     print(text.get('1.0',END))
#     print(entry.get())
#     text.delete('1.0',END)
#     entry.delete(0,END)
#
# btn=Button(w,text='내용 삭제하기',command=clean_text)
# btn.pack()
# w.mainloop()

### 10.마우스 이벤트, 레이블 클릭시 메세지 표시
# from tkinter import *
# w=Tk()
# w.title('GUI 프로그래밍')
# w.geometry('500x200')
# def click_left(event):
#     label.config(text="왼쪽 마우스 클릭")
#
# label=Label(w,text='hello~~~~~')
# label.bind('<Button-1>',click_left)
# # w.bind('<Button-1>',click_left)  # 창 아무데나 클릭시
# label.pack()
# w.mainloop()

### 11.마우스 이벤트, 텍스트 상자 클릭시 내용 지우기
# from tkinter import *
# def clear_text(event):
#     text.delete(1.0, END)
#
# w = Tk()
# w.title('GUI 프로그래밍')
# w.geometry('500x200')
#
# text = Text(w, height=3, width=40, )
# text.pack()
# text.insert(END, "클릭하면 이 텍스트는 지워집니다.")
#
# # 텍스트 상자를 마우스로 클릭할 때 clear_text 함수 호출
# text.bind("<Button-1>", clear_text)
#
# w.mainloop()

### 12.키보드 이벤트, 엔터키를 누르면 엔트리의 내용 지우기
# from tkinter import *
#
# w = Tk()
# w.title('GUI 프로그래밍')
# w.geometry('300x120')
# entry = Entry(w)
# entry.insert(0,"엔터를 누르면 hello가 출력됩니다.")
# entry.pack()
# def on_enter(event):
#     entry.delete(0,END)
#
# w.bind("<Return>", on_enter)
#
# w.mainloop()

### 13,위젯에 글꼴 및 글자 크기, 상하좌우 여백, 정렬 지정하기
# from tkinter import *
# w = Tk()
# w.title('GUI 프로그래밍')
# w.geometry('300x120')
#
# lbl_name=Label(w,text='User Name',width=10,bg='yellow',anchor='w')
# lbl_name.grid(row=0,column=0,padx=30)
# lbl_pwd=Label(w,text='Password',width=10,bg='yellow',anchor='w')
# lbl_pwd.grid(row=1,column=0)
# ent_name=Entry(w,justify='center')   # justify='center' : 가운데 정렬
# ent_name.grid(row=0,column=1,pady=20)
# ent_pwd=Entry(w)
# ent_pwd.grid(row=1,column=1)
#
# w.mainloop()