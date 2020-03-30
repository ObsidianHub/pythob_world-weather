from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from tkinter import messagebox
import time

API_KEY = '8ad22b8e1adc7692cada142aa6f292de'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
# need to add here keys for getting weather details

def get_weather():
  pass

root = ThemedTk(theme='arc')
root.geometry('500x400+1000+300')
root.resizable(0, 0)

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.7, relheight=1)

button = ttk.Button(top_frame, text="Запрос погоды", command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

root.mainloop()