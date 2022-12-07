import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc


'''
Изменение типа столбца
'''
class ChangeType(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Изменение типа столбца')
        self.geometry('300x180')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        field_types = ['integer',
                       'numeric',
                       'character varying',
                       'date']

        self.field_var = tk.StringVar()
        self.field_var.set(field_types[0])

        self.table_name_label = tk.Label(self, text='Введите название таблицы')
        self.table_name_entry = tk.Entry(self)
        self.column_name_label = tk.Label(self, text='Введите название столбца')
        self.column_name_entry = tk.Entry(self)
        self.change_type_label = tk.Label(self, text='Выберите новый тип')
        self.fields_optionmenu = tk.OptionMenu(self, self.field_var, *field_types)
        self.change_type_button = tk.Button(self, text='Изменить тип', command=self.change_type)

        self.table_name_label.pack(fill=tk.X)
        self.table_name_entry.pack(fill=tk.X)
        self.column_name_label.pack(fill=tk.X)
        self.column_name_entry.pack(fill=tk.X)
        self.change_type_label.pack(fill=tk.X)
        self.fields_optionmenu.pack(fill=tk.X)
        self.change_type_button.pack(fill=tk.X)

    def change_type(self):
        if self.table_name_entry.get() == "" or self.column_name_entry.get() == "":
            tk.messagebox.showinfo(title='Ошибка', message='Введите значения')
        else:
            if qc.change_type(self.table_name_entry.get(),
                              self.column_name_entry.get(),
                              self.field_var.get()):
                tk.messagebox.showinfo(title='Успешно', message='Тип изменен')
                self.destroy()
                return
            tk.messagebox.showinfo(title='Ошибка', message='Некорректные данные')
