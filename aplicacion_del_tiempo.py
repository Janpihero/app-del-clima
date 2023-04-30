from tkinter import *
import requests

#6cf2f0050f3f92666af5f36b77ce01ad
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def mostrar_respuesta(clima):
    try:
        nombre_ciudad = clima ["name"]
        desc = clima["weather"][0]["description"]
        temp = clima ["main"]["temp"]

        ciudad["text"] = nombre_ciudad
        temperatura["text"] = str(int(temp)) + "ºC"
        descripcion["text"] = desc
    except:
        ciudad["text"] = "intenta nuevamente"

def clima_json(ciudad):
    try:
        API_key = "6cf2f0050f3f92666af5f36b77ce01ad"
        URL = "https://api.openweathermap.org/data/2.5/weather"
        parametros = {"APPID" : API_key, "q" : ciudad, "units": "metric", "lang": "es"}
        response = requests.get(URL, params = parametros)
        clima = response.json()
        mostrar_respuesta(clima)
    except:
        print("error")


ventana = Tk()
ventana.geometry("350x550")

text_ciudad = Entry(ventana, font = ("Courier", 20, "normal"), justify = "center")
text_ciudad.pack(padx = 30, pady = 30)

obtener_clima = Button(ventana, text = "Obtener clima", font = ("Courier", 20, "normal"), command = lambda: clima_json (text_ciudad.get()))
obtener_clima.pack()

ciudad= Label(font = ("courier", 20, "normal"))
ciudad.pack(padx= 20, pady = 20)

temperatura= Label(font = ("courier", 50, "normal"))
temperatura.pack(padx= 10, pady = 10)

descripcion= Label(font = ("courier", 20, "normal"))
descripcion.pack(padx= 10, pady = 10)



ventana.mainloop()