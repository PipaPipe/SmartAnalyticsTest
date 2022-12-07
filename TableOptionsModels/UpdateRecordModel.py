import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc


'''
Окно для изменения элемента в таблице
'''
class UpdateRecord(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Изменение элемента')
        self.geometry('300x200')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        self.choose_field_label = tk.Label(self, text='Введите поле элемента для поиска')
        self.choose_field_entry = tk.Entry(self)
        self.choose_value_label = tk.Label(self, text='Введите значение поля для поиска')
        self.choose_value_entry = tk.Entry(self)
        self.update_record_label = tk.Label(self, text='Введите поле для изменения')
        self.update_record_entry = tk.Entry(self)
        self.new_value_label = tk.Label(self, text='Введите новое значение')
        self.new_value_entry = tk.Entry(self)
        self.update_button = tk.Button(self, text='Обновить', command=self.update_record)

        self.choose_field_label.pack(fill=tk.X)
        self.choose_field_entry.pack(fill=tk.X)
        self.choose_value_label.pack(fill=tk.X)
        self.choose_value_entry.pack(fill=tk.X)
        self.update_record_label.pack(fill=tk.X)
        self.update_record_entry.pack(fill=tk.X)
        self.new_value_label.pack(fill=tk.X)
        self.new_value_entry.pack(fill=tk.X)
        self.update_button.pack(fill=tk.X)

    def update_record(self):
        element_field = self.choose_field_entry.get()
        element_value = self.choose_value_entry.get()
        update_element = self.update_record_entry.get()
        new_value = self.new_value_entry.get()
        if qc.update_record(element_field, element_value, update_element, new_value):
            tk.messagebox.showinfo(title='Успешно', message='Элемент изменен')
            self.destroy()
            return
        tk.messagebox.showinfo(title='Ошибка', message='Некорректные данные')
