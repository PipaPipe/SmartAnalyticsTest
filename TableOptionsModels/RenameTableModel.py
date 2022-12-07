import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc


'''
Переименование таблицы
'''
class RenameTable(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Изменение названия таблицы')
        self.geometry('300x120')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        self.current_table_label = tk.Label(self, text='Введите название таблицы для изменения')
        self.old_name_entry = tk.Entry(self)
        self.rename_current_table_label = tk.Label(self, text='Введите новое название')
        self.new_name_entry = tk.Entry(self)
        self.rename_table_button = tk.Button(self, text='Переименовать', command=self.rename_table)

        self.current_table_label.pack(fill=tk.X)
        self.old_name_entry.pack(fill=tk.X)
        self.rename_current_table_label.pack(fill=tk.X)
        self.new_name_entry.pack(fill=tk.X)
        self.rename_table_button.pack(fill=tk.X)

    def rename_table(self):
        if self.new_name_entry.get() == "":
            tk.messagebox.showinfo(title='Ошибка', message='Новое имя не может быть пустым')
        else:
            if qc.rename_table(self.old_name_entry.get(),
                               self.new_name_entry.get()):
                tk.messagebox.showinfo(title='Успешно', message='Таблица переименована')
                self.destroy()
                return
            tk.messagebox.showinfo(title='Ошибка', message='Некорректные данные')
