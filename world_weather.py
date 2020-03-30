from tkinter import ttk
from ttkthemes import ThemedTk
import requests
from tkinter import messagebox
import time

API_KEY = '8ad22b8e1adc7692cada142aa6f292de'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
# need to add here keys for getting weather details

def print_weather(weather):
  pass

def get_weather():
  if not entry.get():
    messagebox.showwarning('Warning', 'Введите запрос в формате city, country_code')
  else:
    params = {
      "appid": API_KEY,
      "q": entry.get(),
      "units": "metric",
      "lang": "ru"
    }
    r = requests.get(API_URL, params=params)
    weather = r.json()
    label['text'] = print_weather(weather)

root = ThemedTk(theme='arc')
root.geometry('500x400+1000+300')
root.resizable(0, 0)

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.7, relheight=1)

button = ttk.Button(top_frame, text="Запрос погоды", command=get_weather)
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = ttk.Frame(root)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(lower_frame, anchor='nw')
label.place(relwidth=1, relheight=1)

root.mainloop()