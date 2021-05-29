import matplotlib.pyplot as plotter
import tkinter.font as tkFont
import tkinter as tk
import numpy as np
import threading
from drawnow import *
from SIR_Model import *
from PIL import ImageTk, Image
import tkinter.messagebox as tkMessageBox
from tables import createStandardTable as cst
#-------------------------------------------------------------------------------
def Open_Table():

    secondary_windowN = tk.Tk()
    secondary_windowN.title("Tabla SIR")

    tableFrameN = tk.Frame(secondary_windowN)
    f = open("Tabla_SIR.csv")
    newtableN = cst(f,tableFrameN)
    newtableN.grid()
    tableFrameN.grid()
#-------------------------------------------------------------------------------
def Plot_SIR():
    N = 146800000

    try:
        beta = float(beta_value.get())
    except:
        beta = 0.1
        tkMessageBox.showerror("Error", "ERROR en Beta\nIngrese coeficientes numéricos")
        #Casilla_Beta.delete(0, 'end')
    try:
        gamma = float(gamma_value.get())
    except:
        gamma = 0.1
        tkMessageBox.showerror("Error", "ERROR en Gamma\nIngrese coeficientes numéricos")
        #Casilla_Gamma.delete(0, 'end')
    try:
        Io = int(Spinbox_Io.get())
    except:
        Io = 10
        tkMessageBox.showerror("Error", "ERROR en Io\nIngrese coeficientes ENTEROS")
        #Casilla_Io.delete(0, 'end')


    print("Beta: {}\nGamma: {}\nIo: {}\nN: {}".format(beta, gamma, Io, N))

    So = N - Io
    Ro = 0

    S, I, R = [So], [Io], [Ro]

    to, tf, dt = 0, 200, 1
    T = np.arange(to, tf+dt, dt)


    for t_n in T:

        Runge_Kutta(beta, gamma, N, dSdt, S, t_n, S[-1], I[-1], R[-1], dt)
        Runge_Kutta(beta, gamma, N, dIdt, I, t_n, S[-1], I[-1], R[-1], dt)
        Recovered = N - S[-1] - I[-1]
        if Recovered >= 0:
            R.append(Recovered)
        else:
            R.append(0)

        print("  {}  |  {}  |  {}  |  {}  |  {}  |".format(t_n, S[-1], I[-1], R[-1], S[-1]+I[-1]+R[-1]))

    Create_Table(T, S, I, R)


    plotter.clf()
    plotter.plot(T, S[:-1], '-r', label='Susceptibles')
    plotter.plot(T, I[:-1], '-g', label='Infectados')
    plotter.plot(T, R[:-1], '-b', label='Recuperados')
    plotter.legend(loc=0)
    plotter.title('NUESTRO Modelo SIR COVID-19')
    plotter.xlabel('Días')
    plotter.show()
#-------------------------------------------------------------------------------
main_window = tk.Tk()
main_window.title("Simulación SIR")

canvas = tk.Canvas(main_window, width=852, height=480)
image = ImageTk.PhotoImage(Image.open('Russian_Doge.png'))

canvas.create_image(0,0,anchor='nw', image=image)
canvas.pack()



beta_value = tk.DoubleVar()
gamma_value = tk.DoubleVar()
io_value = tk.DoubleVar()

Slider_Beta = tk.Scale(main_window, from_=0.1, to=1, resolution=0.1, orient='horizontal', tickinterval=1, variable=beta_value)
Slider_Beta.place(x=90, y=80)
label_Beta = tk.Label(main_window, text="Beta: ")
label_Beta.place(x=80, y=100, anchor='ne')

Slider_Gamma = tk.Scale(main_window, from_=0.1, to=1, resolution=0.1, orient='horizontal', tickinterval=1, variable=gamma_value)
Slider_Gamma.place(x=90, y=150)
label_Gamma = tk.Label(main_window, text="Gamma: ")
label_Gamma.place(x=80, y=170, anchor='ne')
""""
Slider_Io = tk.Scale(main_window, from_=1, to=20000001, resolution=1000000, length=300, orient='horizontal', tickinterval=1, variable=io_value)
Slider_Io.place(x=90, y=220)"""
Spinbox_Io = tk.Spinbox(main_window, from_=1, to=146800000, width=15)
Spinbox_Io.place(x=90, y=240)
label_Io = tk.Label(main_window, text="Io: ")
label_Io.place(x=80, y=240, anchor='ne')


N = 146800000

beta = 1/2
gamma = 1/3
Io = 10


button_Graficar = tk.Button(main_window, text='Simular Gráfico', width=20, command=Plot_SIR)
button_Graficar.place(x=750, y=400, anchor='center')

button_Tabla = tk.Button(main_window, text='Mostrar Tabla', width=20, command=Open_Table)
button_Tabla.place(x=750, y=440, anchor='center')


main_window.mainloop()
