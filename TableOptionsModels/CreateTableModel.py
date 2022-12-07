import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc


'''
Окно для создания таблицы
'''
class CreateTable(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Создание таблицы')
        self.geometry('300x260')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        field_types = ['integer',
                       'decimal',
                       'varchar(100)',
                       'date',
                       'varchar(250)']

        self.field_var = tk.StringVar()
        self.field_var.set(field_types[0])

        self.box = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.scroll_box = tk.Scrollbar(command=self.box.yview)

        self.box.pack(side=tk.LEFT)
        self.box.config(yscrollcommand=self.scroll_box.set)

        self.operation_frame = tk.Frame(self)
        self.operation_frame.pack(side=tk.LEFT, padx=10)
        self.table_name_label = tk.Label(self.operation_frame, text='Введите название таблицы')
        self.table_name_entry = tk.Entry(self.operation_frame)
        self.field_label = tk.Label(self.operation_frame, text='Введите название поля')
        self.field_entry = tk.Entry(self.operation_frame)
        self.fields_optionmenu = tk.OptionMenu(self.operation_frame,
                                               self.field_var,
                                               *field_types)
        self.add_field_button  = tk.Button(self.operation_frame,
                                           text='Добавить',
                                           command=self.add_field)
        self.delete_field_button = tk.Button(self.operation_frame,
                                             text='Удалить',
                                             command=self.delete_field)
        self.set_primary_key_button = tk.Button(self.operation_frame,
                                                text='Назначить PKEY',
                                                command=self.set_primary_key)
        self.create_table_button = tk.Button(self.operation_frame,
                                             text='Создать таблицу',
                                             command=self.create_table)

        self.table_name_label.pack(fill=tk.X)
        self.table_name_entry.pack(fill=tk.X)
        self.field_label.pack(fill=tk.X)
        self.field_entry.pack(anchor='n')
        self.fields_optionmenu.pack(fill=tk.X)
        self.add_field_button.pack(fill=tk.X)
        self.delete_field_button.pack(fill=tk.X)
        self.set_primary_key_button.pack(fill=tk.X)
        self.create_table_button.pack(fill=tk.X)

    def add_field(self):
        if self.field_entry.get() == "":
            tk.messagebox.showinfo(title='Ошибка', message='Нельзя добавить пустое поле')
        else:
            self.box.insert(tk.END, [self.field_entry.get(), self.field_var.get()])
            self.field_entry.delete(0, tk.END)

    def delete_field(self):
        select = list(self.box.curselection())
        select.reverse()
        for i in select:
            self.box.delete(i)

    def set_primary_key(self):
        select = list(self.box.curselection())
        select.reverse()
        for i in select:
            if 'K' not in self.box.get(i):
                self.box.insert(i, self.box.get(i) + tuple('K'))
                self.delete_field()

    def create_table(self):
        lst_field = self.box.get(0, tk.END)
        table_name = self.table_name_entry.get()
        if table_name in qc.get_table_names()[1]:
            tk.messagebox.showinfo(title='Ошибка', message=f'Таблица {table_name} уже существует')
        elif table_name == "":
            tk.messagebox.showinfo(title='Ошибка', message='Введите название таблицы')
        elif not lst_field:
            tk.messagebox.showinfo(title='Ошибка', message='Добавьте поля в таблицу')
        else:
            if qc.create_table(table_name, lst_field):
                tk.messagebox.showinfo(title='Успешно', message='Таблица создана')
                self.destroy()
                return
            tk.messagebox.showinfo(title='Ошибка', message='Вы не задали PRIMARY KEY')
