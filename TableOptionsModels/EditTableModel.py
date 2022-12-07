import tkinter as tk

from SupportingModels.ConnectionDecorator import is_table_connection_decorator
from .RenameTableModel import RenameTable
from .RenameColumnModel import RenameColumn
from .AddRecordModel import AddRecord
from .RemoveRecordModel import RemoveRecord
from .UpdateRecordModel import UpdateRecord
from .AddColumnModel import AddColumn
from .DropColumnModel import DropColumn
from .ChangeTypeModel import ChangeType


'''
Окно для изменения данных в таблице
'''
class EditTable(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Изменение таблицы')
        self.geometry('200x210')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        self.add_element_button = tk.Button(self, text='Добавить элемент', command=self.add_record)
        self.remove_element_button = tk.Button(self, text='Удалить элемент', command=self.remove_record)
        self.edit_element_button = tk.Button(self, text='Изменить элемент', command=self.update_record)
        self.rename_table_button = tk.Button(self, text='Изменить название таблицы', command=self.rename_table)
        self.rename_column_button = tk.Button(self, text='Изменить название столбца', command=self.rename_column)
        self.add_column_button = tk.Button(self, text='Добавить столбец', command=self.add_column)
        self.drop_column_button = tk.Button(self, text='Удалить столбец', command=self.drop_column)
        self.change_type_button = tk.Button(self, text='Изменить тип столбца', command=self.change_type)

        self.add_element_button.pack(fill=tk.X)
        self.remove_element_button.pack(fill=tk.X)
        self.edit_element_button.pack(fill=tk.X)
        self.rename_table_button.pack(fill=tk.X)
        self.rename_column_button.pack(fill=tk.X)
        self.add_column_button.pack(fill=tk.X)
        self.drop_column_button.pack(fill=tk.X)
        self.change_type_button.pack(fill=tk.X)

    @staticmethod
    @is_table_connection_decorator
    def add_record():
        AddRecord()

    @staticmethod
    @is_table_connection_decorator
    def remove_record():
        RemoveRecord()

    @staticmethod
    @is_table_connection_decorator
    def update_record():
        UpdateRecord()

    @staticmethod
    def rename_table():
        RenameTable()

    @staticmethod
    def rename_column():
        RenameColumn()

    @staticmethod
    def add_column():
        AddColumn()

    @staticmethod
    def drop_column():
        DropColumn()

    @staticmethod
    def change_type():
        ChangeType()
