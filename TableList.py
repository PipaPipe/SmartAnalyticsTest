import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc
from SupportingModels.ConnectionDecorator import is_db_connection_decorator
from TableListModels.ConnectDatabaseModel import ConnectDatabase


'''
Левый фрейм, содержит в себе кнопку для подключения,
список таблиц в БД
'''
class TablesListFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0)
        self['width'] = 250
        self['height'] = 600
        self['bg'] = '#EBEBEB'
        self.put_widgets()

    def put_widgets(self):
        self.connect_db_button = tk.Button(self, text='Подключиться к БД', command=self.open_dialog)
        self.connect_db_button.pack(anchor='center')

        self.info_frame = tk.Frame(self)
        self.info_frame.pack(fill=tk.BOTH)

        self.current_connection_label = tk.Label(self.info_frame, text='Подключение отсутствует')
        self.tables_list_label = tk.Label(self.info_frame, text='Список таблиц')
        self.tables_list_update_button = tk.Button(self.info_frame, text='Обновить', command=self.update_table_list)

        self.current_connection_label.grid(column=0, row=0, columnspan=2)
        self.tables_list_label.grid(column=0, row=1)
        self.tables_list_update_button.grid(column=1, row=1)

        self.table_list_frame = tk.Frame(self)
        self.table_list_frame.pack()
        self.table_list = tk.Listbox(self.table_list_frame)
        self.table_list.pack(fill=tk.X, side=tk.LEFT)

        self.scroll_table_list = tk.Scrollbar(self.table_list_frame, command=self.table_list.yview)
        self.scroll_table_list.pack(side=tk.LEFT, fill=tk.Y)
        self.table_list.config(yscrollcommand=self.scroll_table_list.set)

    '''
    Обновляем список таблиц в БД
    '''
    @is_db_connection_decorator
    def update_table_list(self):
        self.table_list.delete(0, tk.END)
        self.current_connection_label['text'] = 'Подключено: ' + qc.connection_parameters[4]
        if qc.get_table_names()[0]:
            tables = qc.get_table_names()[1]
            for table_name in tables:
                self.table_list.insert(tk.END, table_name)
        else:
            tk.messagebox.showinfo(title='Ошибка', message='Невозможно обновить список')

    @staticmethod
    def open_dialog():
        ConnectDatabase()
