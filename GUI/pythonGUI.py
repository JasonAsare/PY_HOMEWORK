import customtkinter
from customtkinter import *

window = customtkinter.CTk()
window.geometry("1024x600")
window.title("Jason 0. Asare")

set_appearance_mode("dark")
centerlable = customtkinter.CTkLabel(window, text="Hello World")
centerlable.pack()

window.mainloop()
