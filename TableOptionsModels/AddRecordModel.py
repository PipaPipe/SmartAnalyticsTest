import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc


'''
Окно для добавления элемента в таблицу
'''
class AddRecord(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Добавление элемента')
        self.geometry('400x200')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        self.types_box = tk.Listbox(self)
        self.types_box.pack(side=tk.LEFT)
        if qc.current_table is not None:
            for column_types in qc.get_types()[1]:
                self.types_box.insert(tk.END, column_types)

        self.field_box = tk.Listbox(self, selectmode=tk.EXTENDED)
        self.field_box.pack(side=tk.LEFT)

        self.operation_frame = tk.Frame(self)
        self.operation_frame.pack(side=tk.LEFT, padx=10)

        self.add_field_label = tk.Label(self.operation_frame, text='Введите поле')
        self.add_field_entry = tk.Entry(self.operation_frame)
        self.add_field_button = tk.Button(self.operation_frame, text='Добавить поле', command=self.add_field)
        self.remove_field_button = tk.Button(self.operation_frame, text='Удалить поле', command=self.remove_field)
        self.add_record_button = tk.Button(self.operation_frame, text='Добавить запись', command=self.add_record)

        self.add_field_label.pack(fill=tk.X)
        self.add_field_entry.pack(fill=tk.X)
        self.add_field_button.pack(fill=tk.X)
        self.remove_field_button.pack(fill=tk.X)
        self.add_record_button.pack(fill=tk.X)

    def add_field(self):
        if self.add_field_entry.get() == "":
            tk.messagebox.showinfo(title='ошибка', message='нельзя добавить пустое поле')
        else:
            self.field_box.insert(tk.END, self.add_field_entry.get())
            self.add_field_entry.delete(0, tk.END)

    def remove_field(self):
        select = list(self.field_box.curselection())
        select.reverse()
        for i in select:
            self.field_box.delete(i)

    def add_record(self):
        lst = self.field_box.get(0, tk.END)
        if qc.add_record(lst):
            tk.messagebox.showinfo(title='Успешно', message='Запись добавлена')
            self.field_box.delete(0, tk.END)
            return
        tk.messagebox.showinfo(title='Ошибка', message='Некорректные данные')
