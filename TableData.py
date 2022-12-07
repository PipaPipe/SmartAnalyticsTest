import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from SupportingModels import QueryController as qc
from SupportingModels.ConnectionDecorator import is_db_connection_decorator


'''
Таблица и её содержимое (Центральный фрейм)
'''
class TableDataFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=250, y=0)
        self['width'] = 650
        self['height'] = 600
        self['bg'] = 'white'
        self.put_widgets()

    def put_widgets(self):
        self.user_frame = tk.Frame(self)
        self.table_frame = tk.Frame(self)

        self.user_frame.place(x=0, y=0, width=650, height=40)
        self.table_frame.place(x=0, y=40, width=650, height=560)

        self.get_table_entry = tk.Entry(self.user_frame)
        self.get_table_button = tk.Button(self.user_frame, text='Подключиться', command=self.set_current_table)
        self.current_table_label = tk.Label(self.user_frame, text='Подключено: ')

        self.get_table_entry.grid(column=0, row=0, sticky='nw')
        self.get_table_button.grid(column=1, row=0, sticky='nw')
        self.current_table_label.grid(column=3, row=0, sticky='nw')

        self.table = ttk.Treeview(self.table_frame, show='headings')
        self.table.pack(expand=tk.YES, fill=tk.BOTH)

    @is_db_connection_decorator
    def set_current_table(self):
        if self.get_table_entry.get() in qc.get_table_names()[1]:
            self.current_table_label['text'] = 'Подключено: ' + self.get_table_entry.get()
            self.table.destroy()
            self.table = ttk.Treeview(self.table_frame, show='headings')
            self.table.pack(expand=tk.YES, fill=tk.BOTH)
            qc.current_table = self.get_table_entry.get()
            self.table['columns'] = qc.get_columns_names()[1]
            for header in qc.get_columns_names()[1]:
                self.table.heading(header, text=header, anchor='center')
                self.table.column(header, anchor='center', width=20)
            for row in qc.get_table_records()[1]:
                print(row)
                self.table.insert('', tk.END, values=row)
            return
        tk.messagebox.showinfo(title='Ошибка', message='Такой таблицы не существует')
