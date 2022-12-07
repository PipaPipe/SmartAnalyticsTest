import tkinter as tk

from TableList import TablesListFrame
from TableData import TableDataFrame
from TableOptions import TableOptionsFrame


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Контроллер БД')
        self.put_frames()
        self.geometry('1150x420')
        self.resizable(width=False, height=False)

    def put_frames(self):
        self.frame_tables_list = TablesListFrame(self)
        self.frame_table_data = TableDataFrame(self)
        self.frame_table_options = TableOptionsFrame(self)


app = MainWindow()
app.mainloop()
