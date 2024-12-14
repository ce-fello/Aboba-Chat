import random
from tkinter import *
from tkinter import messagebox
from socket_client import *
from constants import *


class AbobaChatApp:
    """
    Initializes the AbobaChat application.

    :param root: The root Tkinter element
    :type root: Tk
    :param client: The client object for server interaction
    :type client: Client
    """
    def __init__(self, root, client: Client,):
        self.user_id=-1
        self.root = root
        self.client = client
        self.id = -1
        self.root.title("Aboba chat)")
        self.root.geometry("500x500")
        self.root.resizable(width=False, height=False)
        self.root.config(bg='purple')
        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the user interface of the application, including buttons and labels.
        """
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
        """
        Handles the Sign in button click event. 
        Hides the registration button and shows login and password input fields.
        """
        self.btnReg.place_forget()
        self.btnVhod.place_forget()

        self.vveditelogin.place(x=150, y=240, width=200, height=40)
        self.vveditelogin.insert(0, 'Enter the login')
        self.vveditelogin.bind("<Button-1>", self.clear_search_log)

        self.vvediteparol.place(x=150, y=295, width=200, height=40)
        self.vvediteparol.insert(0, 'Enter the password')
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
        """
        Clears the login input field if it contains the placeholder text.
        :param event: The mouse button click event
        :type event: Event
        """
        if self.vveditelogin.get() == 'Enter the login':
            self.vveditelogin.delete(0, END)

    def clear_search_log1(self, event):
        """
        Clears the password input field if it contains the placeholder text.

        :param event: The mouse button click event
        :type event: Event
        """
        if self.vvediteparol.get() == 'Enter the password':
            self.vvediteparol.delete(0, END)

    def Voyti(self):
        """
        Handles the Sign in button click event. 
        Validates user input and attempts to log the user in by sending credentials to the server.

        If the credentials are valid, the user's ID is retrieved and the main window is hidden 
        while the Anketa window is opened.

        :raises: None
        """
        login = self.vveditelogin.get()
        password = self.vvediteparol.get()
        if login != 'Enter the login' and password != 'Enter the password' and login != '' and password != '':
            message = {'key': 'LOGUSER', 'login': login, 'password': password}
            self.client.transfer_data(message)
            if self.client.get_response():
                self.client.transfer_data({'key': 'GETID', 'login': login})
                self.id = self.client.get_data()
                root.withdraw() 
                Anketa(self.root, self.client, self.id)
        else:
            self.vveditedr.place(x=100, y=375, width=300, height=50)

    def clickReg(self):
        """
        Handles the Sign up button click event. 
        Hides the main window and opens the registration window.

        :raises: None
        """
        root.withdraw()
        Registration(self.root, self.client, self.id)


class Registration:
    """
    Initializes the Registration window.

    :param parent: The parent window (main application window).
    :param client: An instance of the Client class to handle server communication.
    :param id: The user ID for the registration process.
    """
    def __init__(self, parent, client: Client, id):
        """
        Initializes the Registration window.

        :param parent: The parent window (main application window).
        :param client: An instance of the Client class to handle server communication.
        :param id: The user ID for the registration process.
        """
        self.parent = parent
        self.client = client
        self.id = id
        self.top = Toplevel(parent)
        self.top.title("Aboba chat")
        self.top.geometry("500x500")
        self.top.resizable(width=False, height=False)
        self.top.config(bg='purple')
        self.setup_ui()
    def init(self, id):
        """
        Initializes the user ID for the registration process.

        :param id: The user ID to be set.
        :raises: None
        """
        self.user_id = id
    def setup_ui(self):
        """
        Sets up the user interface for the registration window. 
        Creates labels, entry fields, and buttons needed for user input.

        :raises: None
        """
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

        self.pridumaytelogin.insert(0, 'Create the login')
        self.pridumaytelogin.bind("<Button-1>", self.clear_search_pridumaytelogin)
        self.pridumaytelogin.place(x=150, y=180, width=200, height=40)

        self.pridumayteparol.insert(0, 'Create the password')
        self.pridumayteparol.bind("<Button-1>", self.clear_search_pridumayteparol)
        self.pridumayteparol.place(x=150, y=235, width=200, height=40)

        self.povtoriteparol.insert(0, 'Repeat the password')
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
        """
        Clears the default text in the login entry field when clicked.

        :param event: The event object associated with the button click.
        :raises: None
        """
        if self.pridumaytelogin.get() == 'Create the login':
            self.pridumaytelogin.delete(0, END)

    def clear_search_pridumayteparol(self, event):
        """
        Clears the default text in the password entry field when clicked.

        :param event: The event object associated with the button click.
        :raises: None
        """
        if self.pridumayteparol.get() == 'Create the password':
            self.pridumayteparol.delete(0, END)

    def clear_search_povtoriteparol(self, event):
        """
        Clears the default text in the repeat password entry field when clicked.

        :param event: The event object associated with the button click.
        :raises: None
        """
        if self.povtoriteparol.get() == 'Repeat the password':
            self.povtoriteparol.delete(0, END)

    def Cont(self):
        """
        Handles the continue button click event. 
        Validates user input and attempts to register a new user by sending credentials to the server.

        If registration is successful, it hides the registration window and opens the profile window.

        :raises: None
        """
        login_1 = self.pridumaytelogin.get()
        password_1 = self.pridumayteparol.get()
        password_2 = self.povtoriteparol.get()
        if login_1 != 'Придумайте логин' and password_1 != 'Придумайте пароль' and \
            login_1 != '' and password_1 != '' and password_1 == password_2:
            if not 4 <= len(login_1) <= 16 and not 6 <= len(password_1) <= 20:
                self.vveditedr.place(x=100, y=375, width=300, height=50)
            message = {'key': 'REGUSER', 'login': login_1, 'password': password_1}
            self.client.transfer_data(message)
            if self.client.get_response():
                self.top.withdraw()
                Profil(self.parent, self.client, self.id)
        else:
            self.lbl1.place(x=100, y=380, width=300, height=30)


class Profil:
    """
    Class that manages a profile window within a larger application. 
    """
    def __init__(self, parent, client: Client, id):
        """
        Initializes the Profil window.

        :param parent: The parent window (main application window).
        :param client: An instance of the Client class to handle server communication.
        :param id: The user ID for the profile.
        """
        self.parent = parent
        self.client = client
        self.id = id
        self.top = Toplevel(parent)
        self.top.title("Aboba chat")
        self.top.geometry("500x500")
        self.top.resizable(width=False, height=False)
        self.top.config(bg='purple')
        self.choice = IntVar(value=0)
        self.setup_ui()    

    def setup_ui(self):
        """
        Sets up the user interface for the profile window. 
        Creates entry fields, labels, radio buttons, and a text area for user input.

        :raises: None
        """
        self.name = Entry(self.top)
        self.surname = Entry(self.top)

        self.name.insert(0, 'Enter your name')
        self.name.bind("<Button-1>", self.clear_search_name)
        self.name.place(x=70, y=100, width=200, height=40)

        self.surname.insert(0, 'Enter your surname')
        self.surname.bind("<Button-1>", self.clear_search_surname)
        self.surname.place(x=70, y=155, width=200, height=40)

        Radiobutton(self.top, text='male', variable=self.choice, value=0).place(x=70, y=210, width=70, height=30)
        Radiobutton(self.top, text='female', variable=self.choice, value=1).place(x=150, y=210, width=70, height=30)

        self.lbl = Label(self.top,
                         text='Write about yourself',
                         font=('Comic Sans MS', 12, 'bold'),
                         bg='purple',
                         fg='white')
        self.lbl.place(y=245, x=60, width=200, height=30)

        self.lbl1 = Label(self.top,
                          text='Please, tell about yourself',
                          font=('Comic Sans MS', 16, 'bold'),
                          bg='purple',
                          fg='white')
        self.lbl1.place(y=30, x=60, width=300, height=50)

        self.info = Text(self.top)
        self.info.place(y=270, x=70, width=360, height=100)

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

        self.lbl1 = Label(self.top,
                          text='Please, fill in the gaps correctly',
                          font=('Comic Sans MS', 10, 'bold'),
                          bg='purple',
                          fg='white')

    def clear_search_name(self, event):
        """
        Clears the default text in the name entry field when clicked.

        :param event: The event object associated with the button click.
        :raises: None
        """
        if self.name.get() == 'Enter your name':
            self.name.delete(0, END)

    def clear_search_surname(self, event):
        """
        Clears the default text in the surname entry field when clicked.

        :param event: The event object associated with the button click.
        :raises: None
        """
        if self.surname.get() == 'Enter your surname':
            self.surname.delete(0, END)

    def back_to_AbobaChatApp(self):
        """
        Closes the profile window and re-displays the parent application window.

        :raises: None
        """
        self.top.destroy()
        self.parent.deiconify()  

    def cont(self):
        """
        Handles the continue button click event.Validates user input and attempts to update user information by sending data to the server.

        If the information is valid and sent successfully, it closes the profile window.

        :raises: None
        """
        if self.name.get() != '' and self.name.get() != 'Enter your name' and \
        self.surname.get() != '' and self.surname.get() != 'Enter your surname':
            name = self.name.get() 
            surname = self.surname.get()
            gender = self.choice.get() # male = 0 female = 1
            info = self.info.get(1.0, END)
            self.top.withdraw()
            self.back_to_AbobaChatApp()
            message = {'key': 'UPDUSERINFO', 'user_id': self.id, 'surname': surname, 'name': name, 'is_male': gender, 'bio': info}
            self.client.transfer_data(message)
            print(name, surname, gender, info)
        else:
            self.lbl1.place(x=100, y=380, width=300, height=30)


class Anketa:
    """
    Class that initializes the Anketa window.

    :param parent: The parent window (main application window).
    :param client: An instance of the Client class to handle server communication.
    :param id: The user ID for the profile.
    """
    def __init__(self, parent, client: Client, id):
        self.parent = parent
        self.client = client
        self.id = id
        self.top1 = Toplevel(parent)
        self.top1.title("Aboba chat")
        self.top1.geometry("500x500")
        self.top1.resizable(width=False, height=False) 
        self.top1.config(bg='purple') 
        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the user interface for the Anketa window. 
        Creates buttons and labels for user interaction.

        :raises: None
        """
        self.btn_edit_prof = Button(self.top1,
                            text='Update profile',
                            command=self.open_edit_profil,
                            font=('Comic Sans MS', 10, 'bold'),
                            fg='black',
                            bg='pink',
                            width=10,
                            height=10,
                            activebackground='pink',
                            activeforeground='blue')
            
        self.btn_edit_prof.place(x=20,y=10,width=100,height=30)

        self.btn_exit = Button(self.top1,
                    text='Log out',
                    command=self.log_out,
                    font=('Comic Sans MS', 10, 'bold'),
                    fg='black',
                    bg='pink',
                    width=10,
                    height=10,
                    activebackground='pink',
                    activeforeground='blue')
        self.btn_exit.place(x=20,y=110,width=100,height=30)

        self.btnChats = Button(self.top1,
                            command=self.open_chats,
                            text='Open chats',
                            font=('Comic Sans MS', 10, 'bold'),
                            bg='pink',
                            fg='black',
                            activebackground='pink',
                            activeforeground='blue')
        self.btnChats.place(x=20,y=60,width=100,height=30)

        self.btn_start_search = Button(self.top1,
                    text='Start search',
                    command=self.start_search,
                    font=('Comic Sans MS', 14, 'bold'),
                    fg='white',
                    bg='pink',
                    width=10,
                    height=10,
                    activebackground='pink',
                    activeforeground='blue')
        self.btn_start_search.place(x=175, y=230, width=150, height=40)

        self.btnlike = Button(self.top1,
                    text='Like',
                    command=self.like,
                    font=('Comic Sans MS', 14, 'bold'),
                    fg='white',
                    bg='pink',
                    width=10,
                    height=10,
                    activebackground='pink',
                    activeforeground='blue')
    
        self.btndislike = Button(self.top1,
                    text='Dislike',
                    command=self.dislike,
                    font=('Comic Sans MS', 14, 'bold'),
                    fg='white',
                    bg='pink',
                    width=10,
                    height=10,
                    activebackground='pink',
                    activeforeground='blue')
      
        self.name = Label(self.top1,
                          text='Name',
                          font=('Comic Sans MS', 10, 'bold'),
                          bg='purple',
                          fg='white')
        
        self.surname = Label(self.top1,
                             text='Surname',
                             font=('Comic Sans MS', 10, 'bold'),
                             bg='purple',
                             fg='white')

        self.gender = Label(self.top1,
                            text='Gender',
                            font=('Comic Sans MS', 10, 'bold'),
                            bg='purple',
                            fg='white')

        self.info = Label(self.top1,
                          text='Bio',
                          font=('Comic Sans MS', 10, 'bold'),
                          bg='purple',
                          fg='white')

        
    def back_to_AbobaChatApp(self):
        """
        Closes the current top-level window and restores the visibility of a parent window.
        """
        self.top1.destroy()
        self.parent.deiconify()

    def log_out(self):
        """
        Logs the user out of the application.

        :raises: None
        """
        self.top1.withdraw()
        self.back_to_AbobaChatApp()

    def start_search(self):
        """
        Initiates a search for other users.

        :raises: None
        """
        message = {'key': 'GETLAST'}
        self.client.transfer_data(message)
        last_id = self.client.get_data()
        id = self.id
        while id == self.id:
            id = random.randint(1, last_id)
        message_bio = {'key': 'GETBIO', 'user_id': id}
        self.client.transfer_data(message_bio)
        result = self.client.get_data()
        self.name.config(text = result[4] )
        self.surname.config(text = result[3])
        if result[5]:
            self.gender.config(text = 'Male')
        else:
            self.gender.config(text = 'Female')
        self.info.config(text = result[6])
        self.name.place(x=150, y=50, width=200, height=40)
        self.surname.place(x=150, y=100, width=200, height=40)
        self.gender.place(x=150, y=150, width=200, height=20)
        self.info.place(x=150, y=180, width=200, height=150)
        self.btn_start_search.place_forget()
        self.btnlike.place(x=100, y=420, width=100, height=40)
        self.btndislike.place(x=300, y=420, width=100, height=40)

    def like(self):
        """
        Sends a like action for a user.

        :raises: None
        """
        message = {'key': 'GETLAST'}
        self.client.transfer_data(message)
        last_id = self.client.get_data()
        id = self.id
        while id == self.id:
            id = random.randint(1, last_id)
        message_bio = {'key': 'GETBIO', 'user_id': id}
        self.client.transfer_data(message_bio)
        result = self.client.get_data()
        self.name.config(text = result[4] )
        self.surname.config(text = result[3])
        if result[5]:
            self.gender.config(text = 'Male')
        else:
            self.gender.config(text = 'Female')
        self.info.config(text = result[6])
        message = {'key': 'CRTCHAT', 'members_id': str(self.id) + ',' + str(id)}
        self.client.transfer_data(message)
        Chat(self.parent, self.client, self.id, id)
        self.add_button()
        
    def dislike(self):
        """
        Sends a dislike action for a user.

        :raises: None
        """
        message = {'key': 'GETLAST'}
        self.client.transfer_data(message)
        last_id = self.client.get_data()
        id = self.id
        while id == self.id:
            id = random.randint(1, last_id)
        message_bio = {'key': 'GETBIO', 'user_id': id}
        self.client.transfer_data(message_bio)
        result = self.client.get_data()
        self.name.config(text = result[4] )
        self.surname.config(text = result[3])
        if result[5]:
            self.gender.config(text = 'Male')
        else:
            self.gender.config(text = 'Female')
        self.info.config(text = result[6])
    
    def come_back(self):
        self.top2.withdraw()
        
    def open_chats(self):
        """
        Opens the chat window.

        :raises: None
        """
        message = {'key': 'GETCHATS', 'user_id': self.id}
        self.client.transfer_data(message)
        self.button_count = self.client.get_data()
        self.top2 = Toplevel()
        self.top2.title("Aboba chat")
        self.top2.geometry("500x500")
        self.top2.resizable(width=False, height=False) 
        self.top2.config(bg='purple')
        self.canvas = Canvas(self.top2)
        self.canvas.config(bg='purple', highlightbackground='purple')
        self.scrollbar = Scrollbar(self.top2, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas,bg='purple')

        self.btn_come_back = Button(self.top2,
                    text='Come back',
                    command=self.come_back,
                    font=('Comic Sans MS', 10, 'bold'),
                    fg='black',
                    bg='pink',
                    width=10,
                    height=10,
                    activebackground='pink',
                    activeforeground='blue')
        self.btn_come_back.place(x=400, y=100, width=80, height=40)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Привязываем полосу прокрутки к канвасу
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Расположение виджетов
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

    def open_edit_profil(self):
        """
        Opens the profile editing window.

        :raises: None
        """
        self.top1.withdraw()
        Change_inf_prof(self.parent, self.client, self.id)

    def open_ch(self, id_partner):
        """
        Creates and opens a new chat window.
        """
        Chat(self.parent, self.client, self.id, id_partner)

    def add_button(self):
        """
        Creates and adds a new button to an existing frame (`self.scrollable_frame`). Each button opens a chat window.
        """
        self.button_count += 1
        button = Button(self.scrollable_frame, text=f"Open chat with {self.button_count}", bg='pink', fg='white',
                        activebackground='pink',
                        activeforeground='blue',
                        command=self.open_ch)
        button.pack(padx=50, pady=5, ipadx=100, ipady=15)  


class Chat:
    """
    Class that represents a chat window within a larger application.
    """
    def __init__(self, parent, client: Client, id_client, id_partner):
        """
        Initializes the Chat window.
        :param parent: The parent window (likely a Tkinter window).
        :type parent: tkinter.Tk or similar
        :param client: A client object for network communication.
        :type client: Client
        :param id_client: The ID of the current user.
        :type id_client: int or str
        :param id_partner: The ID of the chat partner.
        :type id_partner: int or str
        :raises TypeError: if any of the parameters have an incorrect type.
        """
        self.parent = parent
        self.client = client
        self.id = id_client
        self.id_partner = id_partner
        self.chat_id = -1
        self.top3 = Toplevel(parent)
        self.top3.title("Aboba chat")
        self.top3.resizable(width=False, height=False) 
        self.setup_ui()

    def setup_ui(self):
        """
        Sets up the user interface elements of the chat window
        """
        message = {'key': 'GETCHTMB', 'member_id_1': str(self.id), 'member_id_2': str(self.id_partner)}
        self.client.transfer_data(message)
        self.chat_id = self.client.get_data() 
        print(self.chat_id, 'IN SETUP')
        self.label1 = Label(self.top3, bg="pink", fg="black", text="Welcome", font="Helvetica 13 bold", pady=10, width=20, height=1)
        self.label1.grid(row=0)

        self.txt = Text(self.top3, bg="pink", fg="black", font="Helvetica 14", width=60)
        self.txt.grid(row=1, column=0, columnspan=2)

        self.scrollbar = Scrollbar(self.txt)
        self.scrollbar.place(relheight=1, relx=0.974)

        # Привязка scrollbar к текстовому полю
        self.txt.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.txt.yview)

        self.e = Entry(self.top3, bg="pink", fg="black", font="Helvetica 14", width=55)
        self.e.grid(row=2, column=0)

        self.send_button = Button(self.top3, text="Send", font="Helvetica 13 bold", bg="pink", command=self.send)
        self.send_button.grid(row=2, column=1)

    def send(self):
        """
        Sends a message to the chat partner.
        """
        message = self.e.get()
        print(message)
        message_to_server = {'key': 'ADDMSG', 'chat_id': self.chat_id, 'owner_id': self.id, 'message': message}
        print(message_to_server)
        self.client.transfer_data(message_to_server)        
        self.txt.insert(END, "\n" + message)
        self.e.delete(0, END)


class Change_inf_prof(Profil):
    """
    Class that provides a window for changing user profile information
    """
    def __init__(self, parent, client: Client, id):
        """
        Initializes the profile change window.
        :param parent: The parent window (likely a Tkinter window).
        :type parent: tkinter.Tk or similar
        :param client: A client object for handling network communication.
        :type client: Client
        :param id: The ID of the user whose profile is being changed.
        :type id: int or str
        :raises TypeError: if parameters are of incorrect type.
        """
        self.parent = parent
        self.client = client
        self.id = id
        self.top = Toplevel(parent)
        self.top.title("Aboba chat")
        self.top.geometry("500x500")
        self.top.resizable(width=False, height=False)
        self.top.config(bg='purple')
        self.choice = IntVar(value=0)
        self.setup_ui(self.cont)    

    def setup_ui(self, func):
        """
        Sets up the user interface elements
        """
        self.name = Entry(self.top)
        self.surname = Entry(self.top)

        self.name.insert(0, 'Enter your name')
        self.name.bind("<Button-1>", self.clear_search_name)
        self.name.place(x=70, y=100, width=200, height=40)

        self.surname.insert(0, 'Enter your surname')
        self.surname.bind("<Button-1>", self.clear_search_surname)
        self.surname.place(x=70, y=155, width=200, height=40)

        Radiobutton(self.top, text='male', variable=self.choice, value=0).place(x=70, y=210, width=70, height=30)
        Radiobutton(self.top, text='female', variable=self.choice, value=1).place(x=150, y=210, width=70, height=30)

        self.lbl = Label(self.top,
                          text='Write about yourself',
                          font=('Comic Sans MS', 12, 'bold'),
                          bg='purple',
                          fg='white')
        self.lbl.place(y=245, x=60, width= 200, height =30)

        self.lbl1 = Label(self.top,
                          text='Please, tell about yourself',
                          font=('Comic Sans MS', 16, 'bold'),
                          bg='purple',
                          fg='white')
        self.lbl1.place(y=30, x=60, width=300, height=50)

        self.info = Text(self.top)
        self.info.place(y=270, x=70, width= 360, height =100)

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

        self.lbl1 = Label(self.top,
                          text='Please, fill in the gaps correctly',
                          font=('Comic Sans MS', 10, 'bold'),
                          bg='purple',
                          fg='white')

    def clear_search_name(self, event):
        """
        Clears the placeholder text from the name entry field.
        """
        if self.name.get() == 'Enter your name':
            self.name.delete(0, END)

    def clear_search_surname(self, event):
        """
        Clears the placeholder text from the surname entry field.
        """
        if self.surname.get() == 'Enter your surname':
            self.surname.delete(0, END)

    def cont(self):
        """
        Validates the user input and sends the updated profile information to the server if valid.
        """
        if self.name.get() != '' and self.name.get() != 'Enter your name' and \
            self.surname.get() != '' and self.surname.get() != 'Enter your surname':
            name = self.name.get() 
            surname = self.surname.get()
            gender = self.choice.get() # male = 1  female = 0
            info = self.info.get(1.0, END)
            self.top.withdraw()
            Anketa(self.parent, self.client, self.id)
            message = {'key': 'UPDUSERINFO', 'user_id': self.id, 'surname': surname, 'name': name, 'is_male': gender, 'bio': info}
            self.client.transfer_data(message)
            print(name,surname,gender,info)
        else:
            self.lbl1.place(x=100, y=380, width=300, height=30)


if __name__ == "__main__":
    root = Tk()
    client = Client()
    client.start_connection(HOSTNAME, PORT)
    app = AbobaChatApp(root, client)
    root.mainloop()
