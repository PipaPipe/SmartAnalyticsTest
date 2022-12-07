import tkinter as tk
from tkinter import messagebox

import SupportingModels.QueryController as qc


'''
Окно для удаления таблицы
'''
class RemoveTable(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Удаление таблицы')
        self.geometry('300x70')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        self.remove_table_label = tk.Label(self, text="Выберите таблицу для удаления")
        self.remove_table_entry = tk.Entry(self)
        self.remove_table_button = tk.Button(self, text='Удалить таблицу', command=self.remove_table)

        self.remove_table_label.pack(fill=tk.X)
        self.remove_table_entry.pack(fill=tk.X)
        self.remove_table_button.pack(fill=tk.X)

    def remove_table(self):
        table_name = self.remove_table_entry.get()
        if qc.remove_table(table_name):
            tk.messagebox.showinfo(title='Успешно', message='Таблица удалена')
            self.destroy()
            return
        tk.messagebox.showinfo(title='Ошибка', message=f'Таблицы {table_name} не существует')