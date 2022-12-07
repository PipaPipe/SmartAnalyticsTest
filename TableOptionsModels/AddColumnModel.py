import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc


'''
Добавление столбца в таблицу
'''
class AddColumn(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Добавление столбца')
        self.geometry('300x170')
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

        self.table_name_label = tk.Label(self, text='Введите название таблицы')
        self.table_name_entry = tk.Entry(self)
        self.column_name_label = tk.Label(self, text='Введите название нового столбца')
        self.column_name_entry = tk.Entry(self)
        self.field_type_label = tk.Label(self, text='Выберите тип столбца')
        self.fields_optionmenu = tk.OptionMenu(self, self.field_var, *field_types)
        self.add_column_button = tk.Button(self, text='Добавить столбец', command=self.add_column)

        self.table_name_label.pack(fill=tk.X)
        self.table_name_entry.pack(fill=tk.X)
        self.column_name_label.pack(fill=tk.X)
        self.column_name_entry.pack(fill=tk.X)
        self.field_type_label.pack(fill=tk.X)
        self.fields_optionmenu.pack(fill=tk.X)
        self.add_column_button.pack(fill=tk.X)

    def add_column(self):
        if qc.add_column(self.table_name_entry.get(),
                         self.column_name_entry.get(),
                         self.field_var.get()):
            tk.messagebox.showinfo(title='Успешно', message='Столбец добавлен')
            self.destroy()
            return
        tk.messagebox.showinfo(title='Ошибка', message='Некорректные значения')
