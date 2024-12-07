from tkinter import *
root = Tk()#
root.title("Aboba chat)") #заголовок
root.geometry("500x500")# размер
root.resizable(width=False, height=False)#неизменяемость размера
root.iconbitmap("logo.ico")# лого
root.config(bg = 'purple') #фон 1 способ
#root['bg'] = 'black'#фон 2 способ


def click():
    print('Hello')


btn = Button(root, 
             text = 'Вход', #название кнопки
             command = click,#команда по клику
             font = ('Comic Sans MS', 20, 'bold'),#шрифт кнопки, кегль, курсив, жирный
             fg = 'white',#цвет шрифта не в активной фазе
             bg = 'pink',#цвет кнопки
             #width = 10,#параметры кнопки
             #height= 10,#параметры кнопки
             activebackground = 'pink',#цвет кнопки во время нажатия
             activeforeground = 'blue',#цвет шрифта в активной фазе

            )#параметры кнопки

btn1 = Button(root, 
             text = 'Регистрация', #название кнопки
             command = click,#команда по клику
             font = ('Comic Sans MS', 12, 'bold'),#шрифт кнопки, кегль, курсив, жирный
             fg = 'white',#цвет шрифта не в активной фазе
             bg = 'pink',#цвет кнопки
             #width = 11,#параметры кнопки
             #height= 1,#параметры кнопки
             activebackground = 'pink',#цвет кнопки во время нажатия
             activeforeground = 'blue',#цвет шрифта в активной фазе

             )#параметры кнопки




lbl = Label(root,
            text = 'Добро пожаловать в AbobaChat!',
            font = ('Comic Sans MS', 18, 'bold'),
            bg = 'pink',
            fg = 'black')




btn.place(x=175, y=270, width=150, height = 30)
btn1.place(x=175,y=310,width=150, height = 30)
lbl.place(x=50, y=100, width = 400, height = 50)







root.mainloop()











#btn.pack(expand=True,)
#btn.pack(anchor=NW)#метод для отображения кнопки
#btn.pack(fill = None)
#btn.pack(padx = 2, pady = 200)
#btn.pack(anchor="c", pady=170)
#btn1.pack(anchor="c")
#btn.pack(fill=X, padx=[20, 60], pady=30)
#btn1.pack(padx = 5, pady = 5)