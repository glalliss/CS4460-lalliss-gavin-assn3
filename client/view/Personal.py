import tkinter as tk
from client.view.Menu import Menu
from client.service.api import API


class Personal(Menu):
    def __init__(self, master: tk.Frame, root: tk.Tk, *args, **kwargs) -> None:
        super().__init__(master, "Personal", root, *args, **kwargs)

        self.__api = API()
