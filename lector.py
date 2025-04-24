import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
import pyttsx3
import pyperclip

#.Iniciar tts
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

                        #Funciones tts
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def leer_texto():
    texto = entrada.get("1.0", tk.END).strip()
    if texto:
        hablar(texto)

def leer_portapapeles():
    texto = pyperclip.paste().strip()
    if texto:
        hablar(texto)
    else:
        hablar("No hay texto copiado en el portapapeles")

def cargar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, "r", encoding="utf-8") as f:
            contenido = f.read()
            entrada.delete("1.0", tk.END)
            entrada.insert(tk.END, contenido)

def porencima(event, texto):
    hablar(texto)

  #Ventana
ventana = tk.Tk()
ventana.title("Lector de Texto para Discapacidad Visual")
ventana.geometry("500x350")
ventana.resizable(False, False)
ventana.configure(bg="#e0f1ff")

                                                  #Título
etiqueta = tk.Label(ventana, text="Introduce el texto o carga un archivo:", font=("Segoe Print", 12, "bold"), bg="#e0f1ff")
etiqueta.pack(pady=10)
etiqueta.bind("<Enter>", lambda e: porencima(e, "Introduce el texto o carga un archivo"))

                  #Cuadro de texto
entrada = tk.Text(ventana, height=12, width=55, font=("Arial", 10))
entrada.pack(padx=10)

                                                   #Botones
frame_botones = tk.Frame(ventana, bg="#e0f1ff")
frame_botones.pack(pady=30)

btn_leer = tk.Button(frame_botones, text="Leer en voz alta", command=leer_texto, bg="#94b6ff", fg="black", width=20)
btn_leer.pack(side=tk.LEFT, padx=5)
btn_leer.bind("<Enter>", lambda e: porencima(e, "Leer el texto en voz alta"))

btn_cargar = tk.Button(frame_botones, text="Cargar archivo .txt", command=cargar_archivo, bg="#eba4e9", fg="black", width=20)
btn_cargar.pack(side=tk.LEFT, padx=5)
btn_cargar.bind("<Enter>", lambda e: porencima(e, "Cargar archivo de texto"))

btn_portapapeles = tk.Button(frame_botones, text="Leer texto copiado", command=leer_portapapeles, bg="#95d5b2", fg="black", width=20)
btn_portapapeles.pack(side=tk.LEFT, padx=5)
btn_portapapeles.bind("<Enter>", lambda e: porencima(e, "Leer el texto copiado en el portapapeles"))


            #Imagen sonidito
decor_sup_izq = PhotoImage(file="audio.png")
tk.Label(ventana, image=decor_sup_izq, bg="#e0f1ff").place(x=8, y=8)


ventana.mainloop()
