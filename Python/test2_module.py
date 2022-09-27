import B_파일내_단어수정copy
import B_파일합치기
import tkinter as tk
from tkinter import PhotoImage, Button, Label, StringVar, ttk





class test:

    global path1, path2, path3, path4, user_id, password

    path1 = "D:\\Video_Manual\\1.Original\\"
    path2 = "D:\\Video_Manual\\2.Create\\"
    path3 = "D:\\Video_Manual\\GMDS\\"
    path4 = "D:\\Program Files\\Workspace\\picture\\" 



    def Check_word(self):
        print("임시")

    def __init__(self):

        window = tk.Tk()
        window.geometry("490x680+300+150")  # 창 사이즈 + X위치 + Y위치
        window.title('어떤 도움을 드릴까요?                    (Build by KYS & JWS)')
        window.option_add("*Font", "맑은고딕 25")
        window.resizable(False, False)  # 창 X,Y 방향 사이즈 조절 막기

        buttonSize = (80, 70)

        photo1 = PhotoImage(file=f'{path4}exchange.png')
        photo2 = PhotoImage(file=f'{path4}SRT1.png')
        photo3 = PhotoImage(file=f'{path4}SSML1.png')
        photo4 = PhotoImage(file=f'{path4}TXT.png')
        photo5 = PhotoImage(file=f'{path4}XLS1.png')
        photo6 = PhotoImage(file=f'{path4}XLS2.png')
        photo7 = PhotoImage(file=f'{path4}topic1.png')
        photo8 = PhotoImage(file=f'{path4}para2.png')

        message1 = "파일 내의 특정 단어를 치환합니다.\n D:\\Video_Manual\\1.Original\\ 폴더에 파일을 넣으세요.\n ...\\2.Create\\ 폴더에 Changed_(파일명)으로 파일이 만들어집니다."
        message2 = "SRT 파일 내의 원문을 추출합니다.\n D:\\Video_Manual\\2.Create\\ 폴더에 파일을 넣으세요.\n 같은 폴더에 NEW_(파일명)으로 파일이 만들어집니다."
        message3 = "SSML 파일 내의 원문을 추출합니다.\n D:\\Video_Manual\\2.Create\\ 폴더에 파일을 넣으세요.\n 같은 폴더에 파일을 넣으세요.\n ...\\00_Create\\ 폴더에 NEW_(파일명)으로 파일이 만들어집니다."
        message4 = "파일 확장자를 txt로 변경합니다.\n D:\\Video_Manual\\2.Create\\ 폴더에 파일을 넣으세요."
        message5 = "TXT 파일을 엑셀 파일로 신규 생성해 줍니다.\n D:\\Video_Manual\\2.Create\\ 폴더에 파일을 넣으세요."
        message6 = "2D Text 엑셀 파일에 Header를 추가합니다.\n D:\\Video_Manual\\1.Original\\ 폴더에 파일을 넣으세요.\n ...\\2.Create\\ 폴더에 수정된 파일이 만들어집니다."
        message7 = "GMDS에 Topic을 자동 생성합니다.\n D:\\Video_Manual\\GMDS\\ \n 위 폴더에 작업 양식을 기입한 엑셀파일을 넣으세요."
        message8 = "GMDS Topic 내용을 자동 입력합니다.\n D:\\Video_Manual\\GMDS\\ \n 위 폴더에 작업 양식을 기입한 엑셀파일을 넣으세요."

        btn1 = Button(window, image=photo1,height=buttonSize[0], width=buttonSize[1], command=B_파일내_단어수정copy.replace())
        btn1.grid(row=1, column=1)        # btn1.place(x=100,y=100) # x,y position으로 위치시키는 방법은 주석과 같이
        exp1 = Label(window, text=message1, font='Helvetica 10 bold')
        exp1.grid(row=1, column=2)

        btn2 = Button(window, image=photo2,height=buttonSize[0], width=buttonSize[1], command=self.SRT_Clear)
        btn2.grid(row=2, column=1)
        exp2 = Label(window, text=message2, font='Helvetica 10 bold')
        exp2.grid(row=2, column=2)
        window.mainloop()
    

    def SRT_Clear(self):
        print("임시")

test()

