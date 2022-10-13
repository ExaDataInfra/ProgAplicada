import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()
label1 = tk.Label(root, text='Calcular la raiz cuadrada')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)
label2 = tk.Label(root, text='Ingrese el número a calcular:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)
entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)


def getSquareRoot ():

    raiz = entry1.get()
    label3 = tk.Label(root, text= 'El resultado de ' + raiz + ' es:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    label4 = tk.Label(root, text='El resultado es: ' + float(raiz)**0.5,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)

button1 = tk.Button(text='Calcular raiz!', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))

canvas1.create_window(200, 180, window=button1)

root.mainloop()
