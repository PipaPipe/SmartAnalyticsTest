import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc


'''
Удаление столбца из таблицы
'''
class DropColumn(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Удаление столбца')
        self.geometry('300x110')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        self.table_name_label = tk.Label(self, text='Введите название таблицы')
        self.table_name_entry = tk.Entry(self)
        self.column_name_label = tk.Label(self, text='Введите название столбца')
        self.column_name_entry = tk.Entry(self)
        self.drop_column_button = tk.Button(self, text='Удалить столбец', command=self.drop_column)

        self.table_name_label.pack(fill=tk.X)
        self.table_name_entry.pack(fill=tk.X)
        self.column_name_label.pack(fill=tk.X)
        self.column_name_entry.pack(fill=tk.X)
        self.drop_column_button.pack(fill=tk.X)

    def drop_column(self):
        if qc.drop_column(self.table_name_entry.get(),
                          self.column_name_entry.get()):
            tk.messagebox.showinfo(title='Успешно', message='Столбец удален')
            self.destroy()
            return
        tk.messagebox.showinfo(title='Ошибка', message='Не существует такой таблицы/столбца')
