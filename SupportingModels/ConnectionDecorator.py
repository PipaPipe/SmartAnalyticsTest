from tkinter import messagebox

import SupportingModels.QueryController as qc


def is_db_connection_decorator(func):
    def wrapper(*args, **kwargs):
        if qc.is_connection:
            func(*args, **kwargs)
        else:
            messagebox.showinfo(title='Ошибка', message='Подключение отсутствует')
    return wrapper


def is_table_connection_decorator(func):
    def wrapper(*args, **kwargs):
        if qc.current_table:
            func(*args, **kwargs)
        else:
            messagebox.showinfo(title='Ошибка', message='Вы не подключены к таблице')
    return wrapper
