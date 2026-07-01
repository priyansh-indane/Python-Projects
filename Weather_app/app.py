from tkinter import *
from tkinter import ttk
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("OWM_API_KEY") #load env file with api key.

window = Tk()
window.title("Weather App")
window.config(bg="cyan")
window.geometry("700x680")

name_label = Label(window,text="Weather App",font=("Times New Roman",40,"bold"))

name_label.place(x=35,y=20,height=50,width=650)

list_name =  [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",  "Mizoram","Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh", "Uttarakhand",  "West Bengal"]
com = ttk.Combobox(window,values=list_name,font=("Times New Roman",20,"bold"))

com.place(x=35,y=90,height=50,width=650)

w_label = Label(window,text="Weather Climate",font=("Times New Roman",25,"bold"))

w_label.place(x=35,y=220,height=45,width=650)

w_label1 = Label(window,text='',font=("Times New Roman",25,"bold"))

w_label1.place(x=35,y=265,height=45,width=650)

wb_label = Label(window,text="Weather description",font=("Times New Roman",25,"bold"))

wb_label.place(x=35,y=320,height=45,width=650)

wb_label1 = Label(window,text='',font=("Times New Roman",25,"bold"))

wb_label1.place(x=35,y=365,height=45,width=650)

temp_label = Label(window,text="Temperatue",font=("Times New Roman",25,"bold"))

temp_label.place(x=35,y=420,height=45,width=650)

temp_label1 = Label(window,text='',font=("Times New Roman",25,"bold"))

temp_label1.place(x=35,y=465,height=45,width=650)

pre_label = Label(window,text="Pressure ",font=("Times New Roman",25,"bold"))

pre_label.place(x=35,y=520,height=45,width=650)

pre_label1 = Label(window,text='',font=("Times New Roman",25,"bold"))

pre_label1.place(x=35,y=565,height=45,width=650)

def get_weather(): # get weather using api key
    city_name = com.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+API_KEY+"&units=metric").json()
    print(data)

    if data.get("cod") != 200:
        w_label1.config(text=data.get("message","City not found"))
        wb_label1.config(text='')
        temp_label1.config(text='')
        pre_label1.config(text='')
        return

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(data["main"]["temp"])+" °C")
    pre_label1.config(text=str(data["main"]["pressure"])+" hPa")

done_button = Button(window,text="Done",font=("Times New Roman",20,"bold"),command=get_weather)

done_button.place(y=150 , height=50 , width=300,x=200)

window.mainloop()