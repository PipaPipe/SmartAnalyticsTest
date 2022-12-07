import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc


'''
Переименование столбца
'''
class RenameColumn(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Изменение названия таблицы')
        self.geometry('300x160')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        self.table_name_label = tk.Label(self, text='Введите название таблицы')
        self.table_name_entry = tk.Entry(self)
        self.old_column_name_label = tk.Label(self, text='Введите название столбца для изменения')
        self.old_column_name_entry = tk.Entry(self)
        self.new_column_name_label= tk.Label(self, text='Введите новое название столбца')
        self.new_column_name_entry = tk.Entry(self)
        self.rename_column_button = tk.Button(self, text='Переименовать', command=self.rename_column)

        self.table_name_label.pack(fill=tk.X)
        self.table_name_entry.pack(fill=tk.X)
        self.old_column_name_label.pack(fill=tk.X)
        self.old_column_name_entry.pack(fill=tk.X)
        self.new_column_name_label.pack(fill=tk.X)
        self.new_column_name_entry.pack(fill=tk.X)
        self.rename_column_button.pack(fill=tk.X)

    def rename_column(self):
        if qc.rename_column(self.table_name_entry.get(),
                            self.old_column_name_entry.get(),
                            self.new_column_name_entry.get()):
            tk.messagebox.showinfo(title='Успешно', message='Столбец переименован')
            self.destroy()
            return
        tk.messagebox.showinfo(title='Ошибка', message='Не существует такой таблицы/столбца')
