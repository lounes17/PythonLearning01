

from tkinter import *
import serial
arduinodata=serial.Serial('COM3', 9600)
def led_on():
             arduinodata.write(b'a')
def led_off():
            arduinodata.write(b'b')


window = Tk()
window.title("CLS_TIZI_OUZOU")
window.geometry("720x480")
window.minsize(480, 360)
window.config(background='gray')
window.iconbitmap('ico.ico')
frame=Frame(window, bg='gray')
Label(frame, text="CLS TIZI OUZOU ", font=("Courrier", 40), bg='gray', fg='#36424d').pack()
Label(frame, text="MONSIEUR ABBAR LOUNES ", font=("Courrier", 15), bg='gray', fg='#36424d').pack()
Label(frame, text="MONSIEUR KHATI SAMIR ", font=("Courrier", 15), bg='gray', fg='#36424d').pack()


button = Button(frame, text="ON", font=("Courrier", 15), fg='#36424d',command=led_on).pack(pady=25, fill=X)
button1 = Button(frame, text="OFF", font=("Courrier", 15), fg='#36424d', command=led_off).pack(pady=25, fill=X)

frame.pack(expand=YES)

window.mainloop()

