from tkinter import *
from tkinter import messagebox


class AbobaChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aboba chat)")
        self.root.geometry("500x500")
        self.root.resizable(width=False, height=False)
        #self.root.iconbitmap("../resources/logo.ico")
        self.root.config(bg='purple')
        self.setup_ui()
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
    
    def on_closing(self):
        if messagebox.askokcancel('Выход из приложения', 'Хотите выйти из приложения?'):
            self.root.destroy()

    def setup_ui(self):

        self.btnVhod = Button(self.root,
                              text='Sign in',
                              command=self.clickVhod,
                              font=('Comic Sans MS', 20, 'bold'),
                              fg='white',
                              bg='pink',
                              activebackground='pink',
                              activeforeground='blue')
        self.btnVhod.place(x=150, y=270, width=200, height=40)

        self.lbl = Label(self.root,
                         text='Welcome to the AbobaChat!', 
                         font=('Comic Sans MS', 20, 'bold'),
                         bg='purple',
                         fg='white')
        self.lbl.place(x=50, y=100, width=400, height=50)

        self.btnReg = Button(self.root,
                             text='Sign up',
                             command=self.clickReg,
                             font=('Comic Sans MS', 20, 'bold'),
                             fg='white',
                             bg='pink',
                             activebackground='pink',
                             activeforeground='blue')
        self.btnReg.place(x=150, y=325, width=200, height=40)

        self.autorization = Label(self.root,
                                text='Authorization', 
                                font=('Comic Sans MS', 20, 'bold'),
                                bg='purple',
                                fg='white')

        self.vveditelogin = Entry(self.root)
        self.vvediteparol = Entry(self.root)

        self.vveditedr = Label(self.root,
                            text='Please, fill in the gaps correctly',
                            font=('Comic Sans MS', 10, 'bold'),
                            bg='purple',
                            fg='white')

    def clickVhod(self):
        self.btnReg.place_forget()
        self.btnVhod.place_forget()

        self.vveditelogin.place(x=150, y=240, width=200, height=40)
        self.vveditelogin.insert(0, 'Введите логин')
        self.vveditelogin.bind("<Button-1>", self.clear_search_log)

        self.vvediteparol.place(x=150, y=295, width=200, height=40)
        self.vvediteparol.insert(0, 'Введите пароль')
        self.vvediteparol.bind("<Button-1>", self.clear_search_log1)

        self.autorization.place(x=50, y=170, width=400, height=50)

        self.btnVoyti = Button(self.root,
                               text='Sign in',
                               command=self.Voyti,
                               font=('Comic Sans MS', 20, 'bold'),
                               fg='white',
                               bg='pink',
                               activebackground='pink',
                               activeforeground='blue')
        self.btnVoyti.place(x=150, y=350, width=200, height=40)

    def clear_search_log(self, event):
        if self.vveditelogin.get() == 'Введите логин':
            self.vveditelogin.delete(0, END)

    def clear_search_log1(self, event):
        if self.vvediteparol.get() == 'Введите пароль':
            self.vvediteparol.delete(0, END)

    def Voyti(self):
        login = self.vveditelogin.get()
        parol = self.vvediteparol.get()
        if login != 'Введите логин' and parol != 'Введите пароль' and login != '' and parol !='':#проверка на базу данных
            root.withdraw() 
            Profil(self.root)
        else:
            self.vveditedr.place(x=100, y=375, width=300, height=50)

    def clickReg(self):
        root.withdraw()
        Registration(self.root)
        


class Registration:
    def __init__(self, parent):
        self.parent = parent
        self.top=Toplevel(parent)
        self.top.title("Aboba chat")
        self.top.geometry("500x500")
        self.top.resizable(width=False, height=False)
        #self.top.iconbitmap("../resources/logo.ico")
        self.top.config(bg='purple')
        self.setup_ui()
        

    def setup_ui(self):
        self.lbl = Label(self.top,
                         text='Registration',
                         font=('Comic Sans MS', 26, 'bold'),
                         bg='purple',
                         fg='white')
        self.lbl.place(x=50, y=100, width=400, height=50)

        self.lbl1 = Label(self.top,
                          text='Please, fill in the gaps correctly',
                          font=('Comic Sans MS', 10, 'bold'),
                          bg='purple',
                          fg='white')

        self.pridumaytelogin = Entry(self.top)
        self.pridumayteparol = Entry(self.top)
        self.povtoriteparol = Entry(self.top)

        self.pridumaytelogin.insert(0,'Придумайте логин' )
        self.pridumaytelogin.bind("<Button-1>", self.clear_search_pridumaytelogin)
        self.pridumaytelogin.place(x=150, y=180, width=200, height=40)

        self.pridumayteparol.insert(0, 'Придумайте пароль')
        self.pridumayteparol.bind("<Button-1>", self.clear_search_pridumayteparol)
        self.pridumayteparol.place(x=150, y=235, width=200, height=40)

        self.povtoriteparol.insert(0, 'Повторите пароль')
        self.povtoriteparol.bind("<Button-1>", self.clear_search_povtoriteparol)
        self.povtoriteparol.place(x=150, y=290, width=200, height=40)

        


        self.btnCont = Button(self.top,
                              text='Продолжить',
                              command=self.Cont,
                              font=('Comic Sans MS', 14, 'bold'),
                              fg='white',
                              bg='pink',
                              width=10,
                              height=10,
                              activebackground='pink',
                              activeforeground='blue')
        self.btnCont.place(x=150, y=345, width=200, height=40)


    def clear_search_pridumaytelogin(self, event):
        if self.pridumaytelogin.get() == 'Придумайте логин':
            self.pridumaytelogin.delete(0, END)

    def clear_search_pridumayteparol(self, event):
        if self.pridumayteparol.get() == 'Придумайте пароль':
            self.pridumayteparol.delete(0, END)

    def clear_search_povtoriteparol(self, event):
        if self.povtoriteparol.get() == 'Повторите пароль':
            self.povtoriteparol.delete(0, END)

    

    def back_to_AbobaChatApp(self):
        self.top.destroy()  # Закрыть окно регистрации
        self.parent.deiconify()  # Показать основное окно снова


    def Cont(self):
        login1 = self.pridumaytelogin.get()
        parol1 = self.pridumayteparol.get()
        parol2=self.povtoriteparol.get()

        if login1 != 'Придумайте логин' and parol1 != 'Придумайте пароль' and login1 !='' and parol1 !='' and parol1 == parol2: #проверка на повторную регистрацию
            self.top.after(500, self.back_to_AbobaChatApp)
            print(login1,parol1) # исправить на return
        else:
            self.lbl1.place(x=100, y=380, width=300, height=30)

class Profil:
    def __init__(self, parent):
        self.parent = parent
        self.top=Toplevel(parent)
        self.top.title("Aboba chat")  # Заголовок
        self.top.geometry("500x500")  # Размер
        self.top.resizable(width=False, height=False)  # Неизменяемость размера
        #self.top.iconbitmap("../resources/logo.ico")  # Лого
        self.top.config(bg='purple')  # Фон
        self.choice=IntVar(value='male')
        self.setup_ui()    

    def setup_ui(self):
        self.name=Entry(self.top)
        self.surname=Entry(self.top)

        self.name.insert(0,'Enter your name' )
        self.name.bind("<Button-1>", self.clear_search_name)
        self.name.place(x=70, y=100, width=200, height=40)

        self.surname.insert(0,'Enter your surname')
        self.surname.bind("<Button-1>", self.clear_search_surname)
        self.surname.place(x=70, y=155, width=200, height=40)

        Radiobutton(self.top, text='male', variable=self.choice, value='male').place(x=70, y=210, width=70, height=30)
        Radiobutton(self.top, text='female', variable=self.choice, value='female').place(x=150, y=210, width=70, height=30)

        self.lbl=Label(self.top,
                          text='Write about yourself',
                          font=('Comic Sans MS', 12, 'bold'),
                          bg='purple',
                          fg='white')
        self.lbl.place(y=255, x=60, width= 200, height =30)

        self.lbl1=Label(self.top,
                          text='Please, tell about yourself',
                          font=('Comic Sans MS', 16, 'bold'),
                          bg='purple',
                          fg='white')
        self.lbl1.place(y=30, x=60, width= 300, height =50)


        self.info=Text(self.top)
        self.info.place(y=300, x=70, width= 360, height =100)

        self.btnregprof = Button(self.top,
                              text='Continue',
                              command=self.cont,
                              font=('Comic Sans MS', 14, 'bold'),
                              fg='white',
                              bg='pink',
                              width=10,
                              height=10,
                              activebackground='pink',
                              activeforeground='blue')
        self.btnregprof.place(x=150, y=420, width=200, height=40)

    
    def clear_search_name(self, event):
        if self.name.get() == 'Enter your name':
            self.name.delete(0, END)
    def clear_search_surname(self, event):
        if self.surname.get() == 'Enter your surname':
            self.surname.delete(0, END)

    def cont(self):
        name=self.name.get() 
        surname=self.surname
        gender=self.choice
        Anketa(self.parent)
        print(name)

        


class Anketa:
    def __init__(self, parent):
        self.parent = parent
        self.top=Toplevel(parent)
        self.top.title("Aboba chat")  # Заголовок
        self.top.geometry("500x500")  # Размер
        self.top.resizable(width=False, height=False)  # Неизменяемость размера
        #self.top.iconbitmap("../resources/logo.ico")  # Лого
        self.top.config(bg='purple')  # Фон
        #self.setup_ui()


if __name__ == "__main__":
    root = Tk()
    app = AbobaChatApp(root)
    root.mainloop()