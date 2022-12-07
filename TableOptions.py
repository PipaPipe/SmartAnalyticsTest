import tkinter as tk

from SupportingModels.ConnectionDecorator import is_db_connection_decorator
from TableOptionsModels.CreateTableModel import CreateTable
from TableOptionsModels.RemoveTableModel import RemoveTable
from TableOptionsModels.EditTableModel import EditTable


'''
Все функции для редактирования таблиц (Правый фрейм)
'''
class TableOptionsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=900, y=0)
        self['width'] = 250
        self['height'] = 600
        self['bg'] = '#EBEBEB'
        self.put_widgets()

    def put_widgets(self):
        self.edit_table_button = tk.Button(self, text='Редактировать таблицу', command=self.edit_table_dialog)
        self.create_table_button = tk.Button(self, text='Создать таблицу', command=self.create_table_dialog)
        self.remove_table_button = tk.Button(self, text='Удалить таблицу', command=self.remove_table_dialog)

        self.edit_table_button.place(x=10, y=10)
        self.create_table_button.place(x=10, y=50)
        self.remove_table_button.place(x=10, y=90)

    @staticmethod
    @is_db_connection_decorator
    def create_table_dialog():
        CreateTable()

    @staticmethod
    @is_db_connection_decorator
    def edit_table_dialog():
        EditTable()

    @staticmethod
    @is_db_connection_decorator
    def remove_table_dialog():
        RemoveTable()
