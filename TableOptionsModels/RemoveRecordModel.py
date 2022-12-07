import tkinter as tk
from tkinter import messagebox

from SupportingModels import QueryController as qc


'''
Окно для удаления элемента из таблицы
'''
class RemoveRecord(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_dialog()
        self.put_widgets()

    def init_dialog(self):
        self.title('Удаление элемента')
        self.geometry('250x140')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

    def put_widgets(self):
        self.remove_record_field_label = tk.Label(self, text=f'Введите поле элемента\n'
                                                        f'для удаления в таблице {qc.current_table}')
        self.remove_record_field_entry = tk.Entry(self)

        self.remove_record_value_label = tk.Label(self, text='Введите значение поля')
        self.remove_record_value_entry = tk.Entry(self)
        self.remove_record_button = tk.Button(self, text='Удалить', command=self.remove_record)

        self.remove_record_field_label.pack(fill=tk.X)
        self.remove_record_field_entry.pack(fill=tk.X)
        self.remove_record_value_label.pack(fill=tk.X)
        self.remove_record_value_entry.pack(fill=tk.X)
        self.remove_record_button.pack(fill=tk.X)

    def remove_record(self):
        element_field = self.remove_record_field_entry.get()
        element_value = self.remove_record_value_entry.get()
        if qc.remove_record(element_field, element_value):
            tk.messagebox.showinfo(title='Успешно', message='Элемент был удален')
            self.remove_record_value_entry.delete(0, tk.END)
            self.remove_record_field_entry.delete(0, tk.END)
            return
        tk.messagebox.showinfo(title='Ошибка', message=f'В таблице нет записи с {element_field}={element_value}')
