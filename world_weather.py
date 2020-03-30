from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from tkinter import messagebox
import time

API_KEY = '8ad22b8e1adc7692cada142aa6f292de'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
# need to add here keys for getting weather details

root = ThemedTk(theme='arc')
root.geometry('500x400+1000+300')
root.resizable(0, 0)

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

root.mainloop()