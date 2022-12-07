import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc

'''
Окно для подключения к БД
установка параметров для подключения
'''
class ConnectDatabase(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Подключиться к БД')
        self.geometry('270x252')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        self.connect_db_label = tk.Label(self, text='Подключение к БД')
        self.user_label = tk.Label(self, text='Имя пользователя')
        self.password_label = tk.Label(self, text='Пароль')
        self.host_label = tk.Label(self, text='Хост')
        self.port_label = tk.Label(self, text='Порт')
        self.db_label = tk.Label(self, text='Имя БД')
        self.connect_database_button = tk.Button(self, text='Подключиться', command=self.set_connect_parameters)

        self.user_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show='*')
        self.host_entry = tk.Entry(self)
        self.port_entry = tk.Entry(self)
        self.db_entry = tk.Entry(self)

        self.connect_db_label.grid(column=0, row=0, sticky='nsew', columnspan=2)
        self.user_label.grid(column=0, row=1, sticky='w', padx=10, pady=10)
        self.password_label.grid(column=0, row=2, sticky='w', padx=10, pady=10)
        self.host_label.grid(column=0, row=3, sticky='w', padx=10, pady=10)
        self.port_label.grid(column=0, row=4, sticky='w', padx=10, pady=10)
        self.db_label.grid(column=0, row=5, sticky='w', padx=10, pady=10)

        self.user_entry.grid(column=1, row=1, sticky='e', padx=10, pady=10)
        self.password_entry.grid(column=1, row=2, sticky='e', padx=10, pady=10)
        self.host_entry.grid(column=1, row=3, sticky='e', padx=10, pady=10)
        self.port_entry.grid(column=1, row=4, sticky='e', padx=10, pady=10)
        self.db_entry.grid(column=1, row=5, sticky='e', padx=10, pady=10)
        self.connect_database_button.grid(column=0, row=6, sticky='nsew', columnspan=2)

    '''
    Метод для установки соединения с БД
    '''
    def set_connect_parameters(self):
        user = self.user_entry.get()
        password = self.password_entry.get()
        host = self.host_entry.get()
        port = self.port_entry.get()
        database = self.db_entry.get()
        qc.connection_parameters = [user, password, host, port, database]
        if qc.set_connection():
            tk.messagebox.showinfo(title="Подключение", message="Подключение выполнено")
            qc.is_connection = True
            self.destroy()
            return
        tk.messagebox.showinfo(title="Ошибка", message="Некорректные данные")
