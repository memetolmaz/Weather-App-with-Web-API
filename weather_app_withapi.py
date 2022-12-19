import tkinter as tk
import requests
import time

def getweather(canvas):
    city = textfield.get() 
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=3e263358c3d29a8fe9e945debcba1d46"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    feels_like = (json_data['main']['feels_like'] - 273.15 )
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']- 32400 ))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']- 32400 ))
    #speed = str(json_data['wind']['speed'])


    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n"  + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Feels Like: " + str(feels_like) +  "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset + "\n" 
    label1.config(text = final_info)
    label2.config(text = final_data)

 
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")


f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, justify='center', width = 20,  font = t)
textfield.pack(pady= 20)
textfield.focus()
textfield.bind('<Return>',getweather)

label1 = tk.Label(canvas , font = t)
label1.pack()
label2 = tk.Label(canvas , font= f)
label2.pack()

canvas.mainloop()



 