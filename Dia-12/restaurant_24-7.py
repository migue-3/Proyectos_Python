from tkinter import  *
import random
import datetime
from tkinter import filedialog, messagebox
from fpdf import FPDF

# Variable para almacenar los numeros que se vayan presionando
# en la calculadora antes de borrar o emitir el resultado
operador = ''

# Listas de precios
precios_comida = [10.32, 11.65, 15.31, 8.22, 6.22, 9.99, 20.05, 13.65]
precios_bebida = [2.25, 2.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58, 5.00, 1.33, 1.23]
precios_postres = [11.54, 10.68, 3.32, 2.00, 2.55, 24.14, 4.94, 10.74]

# Funcion que se invoca cada vez que se presiona un boton de la calculadora
def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    for x in reversed(range(len(cuadros_comidas))):
        if variables_comidas[x].get() == 1:
            cuadros_comidas[x].config(state=NORMAL)
            if cuadros_comidas[x].get() == "0":
                cuadros_comidas[x].delete(0, END)
                cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state=DISABLED)
            texto_comidas[x].set("0")

    for x in reversed(range(len(cuadros_bebidas))):
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == "0":
                cuadros_bebidas[x].delete(0, END)
                cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set("0")

    for x in reversed(range(len(cuadros_postres))):
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == "0":
                cuadros_postres[x].delete(0, END)
                cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set("0")


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comidas:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebidas = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebidas = sub_total_bebidas + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total_pedido = sub_total_comida + sub_total_bebidas + sub_total_postres
    impuestos = sub_total_pedido * 0.07
    total_pedido = sub_total_pedido + impuestos

    var_precio_comida.set(f"$ {round(sub_total_comida, 2)}")
    var_precio_bebida.set(f"$ {round(sub_total_bebidas, 2)}")
    var_precio_postre.set(f"$ {round(sub_total_postres, 2)}")
    var_subtotal.set(f"$ {round(sub_total_pedido, 2)}")
    var_iva.set(f"$ {round(impuestos, 2)}")
    var_total.set(f"$ {round(total_pedido, 2)}")


def generar_factura():
    # Asegurar que el ticket quede completamente en blanco para generar el nuevo ticket
    texto_factura.delete(1.0, END)
    num_factura = f"nro - {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_factura = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_factura.insert(END, f'Datos# {num_factura}\t\t{fecha_factura}\n')
    texto_factura.insert(END, f'*' * 44 + '\n')
    texto_factura.insert(END, f'Items\t  Cant.\tCosto Items\n')
    texto_factura.insert(END, f'-' * 56 + '\n')

    x = 0
    for comida in texto_comidas:
        # Llamamos al metodo get() para obtener el valor actual
        if variables_comidas[x].get() == 1 and comida.get() != '0':
            texto_factura.insert(END, f"{lista_comidas[x]}\t{comida.get()}\t"
                                      f"\t${int(comida.get()) * precios_comida[x]}\n")
        x += 1

    x = 0
    for bebida in texto_bebidas:
        # Llamamos al metodo get() para obtener el valor actual
        if variables_bebidas[x].get() == 1 and bebida.get() != '0':
            texto_factura.insert(END, f"{lista_bebidas[x]}\t{bebida.get()}\t"
                                      f"\t${int(bebida.get()) * precios_bebida[x]}\n")
        x += 1

    x = 0
    for postre in texto_postres:
        # Llamamos al metodo get() para obtener el valor actual
        if variables_postres[x].get() == 1 and postre.get() != '0':
            texto_factura.insert(END, f"{lista_postres[x]}\t{postre.get()}\t"
                                      f"\t${int(postre.get()) * precios_postres[x]}\n")
        x += 1

    texto_factura.insert(END, f'-' * 56 + '\n')
    texto_factura.insert(END, f'Costo de la comida: \t\t{var_precio_comida.get()}\n')
    texto_factura.insert(END, f'Costo de la bebida: \t\t{var_precio_bebida.get()}\n')
    texto_factura.insert(END, f'Costo del postre: \t\t{var_precio_postre.get()}\n')
    texto_factura.insert(END, f'-' * 56 + '\n')
    texto_factura.insert(END, f'Sub-total: \t\t{var_subtotal.get()}\n')
    texto_factura.insert(END, f'Iva%: \t\t{var_iva.get()}\n')
    texto_factura.insert(END, f'Total: \t\t{var_total.get()}\n')
    texto_factura.insert(END, f'*' * 44 + '\n')
    texto_factura.insert(END, "Lo esperamos pronto!!")


def guardar():
    # Crear instancia de FPDF que usaremos para generar el PDF
    pdf = FPDF()
    pdf.add_page()

    # Establecer fuente
    pdf.set_font("Arial", size=12)

    # Agregar información de la factura
    info_factura = texto_factura.get(1.0, END)
    lineas = info_factura.split('\n')
    for linea in lineas:
        pdf.cell(200, 10, txt=linea, ln=True)

    # Guardar el PDF en un archivo
    ruta_archivo = filedialog.asksaveasfilename(defaultextension='.pdf')
    if ruta_archivo:  # Verificar si se dio una ruta válida
        pdf.output(ruta_archivo)
        messagebox.showinfo('Información', 'Su factura ha sido guardada como PDF!')
    else:
        messagebox.showerror('Error', 'No se especificó un archivo válido.')

    #  Tenemos la factura y la guardamos en una variable
    # info_factura = texto_factura.get(1.0, END)
    # archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    # archivo.write(info_factura)
    # archivo.close()
    # messagebox.showinfo('Informacion', 'Su factura ha sido guardada!!')


def reset():
    texto_factura.delete(0.1, END)

    for texto in texto_comidas:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comidas:
        v.set(0)
    for v in variables_bebidas:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    var_precio_comida.set('')
    var_precio_bebida.set('')
    var_precio_postre.set('')
    var_subtotal.set('')
    var_iva.set('')
    var_total.set('')

# Inicializar tkinter
aplicacion = Tk()

# Dimensiones de la pantalla
aplicacion.geometry('1200x650+0+0')

# Evitar que se pueda maximizar la ventana
aplicacion.resizable(False, False)

# Titulo de la ventana
aplicacion.title("Restaurant 24-7 - Sistema de Facturación")

# Establecer color de fondo de la ventana
aplicacion.config(bg='burlywood')

# Panel superior
panel_superior = Frame(aplicacion, bd=1.5, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta para el titulo del panel_superior
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación / 24-7', fg='honeydew',
                        font=('Dosis', 40), bg='burlywood4', width=32)
etiqueta_titulo.grid(row=0, column= 0)

# Panel izquierdo (menu)
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel de precios
panel_precios = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='burlywood4', padx=100)
panel_precios.pack(side=BOTTOM)

# Panel de comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Platos principales', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='brown', width=300)
panel_comidas.pack(side=LEFT, fill='both', expand=True)

# Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='brown', width=300)
panel_bebidas.pack(side=LEFT, fill='both', expand=True)

# Panel de postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='brown', width=300)
panel_postres.pack(side=LEFT, fill='both', expand=True)

# Panel de la derecha
panel_derecha = Frame(aplicacion, bd=1.5, relief=FLAT, bg='burlywood4')
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood4')
# si no ponemos nada dentro de los () de pack por defecto lo ubica arriba de la ventana
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood4')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood4')
panel_botones.pack()

# Lista de productos
lista_comidas = ['Pollo a la plancha', 'Merluza a la romana', 'Pizza 420', 'Pasta con camaroes',
                 'Pollo broaster', 'Costillas BBQ', 'Shawarma', 'Sopa de res']
lista_bebidas = ['Batido maracuya', 'Batido frutilla', 'Fanta', 'Coca', 'Limonada', 'Sprite',
                 'Exprimido de naranja', 'Cervezas', 'Agua', 'Fernet', 'Vino']
lista_postres = ['Torta tres leches', 'Helado', 'Budin chocolate', 'Churros 420', 'Brownies',
                 'Torta matilda (triple chocolate)', 'Tartaleta frutilla', 'Profiteroles']

# Crear checkbuttons mediante un loop que vaya iterando por cada producto
# para cargar cada uno de los nombres de los productos en el panel que corresponde
# Generar items comidas
variables_comidas = []
cuadros_comidas = []
texto_comidas = []
contador = 0
for comida in lista_comidas:

    # Crear checkbuttons
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 15, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comidas[contador],
                         command=revisar_check)
    # Ubicar los checkbuttons dentro del respectivo panel
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear cuadros de entrada
    cuadros_comidas.append('')
    texto_comidas.append('')
    texto_comidas[contador] = StringVar()
    texto_comidas[contador].set('0')
    cuadros_comidas[contador] = Entry(panel_comidas,
                                      font=('Dosis', 15, 'bold'),
                                      bd=1,
                                      width=4,
                                      state=DISABLED,
                                      textvariable=texto_comidas[contador])
    cuadros_comidas[contador].grid(row=[contador],
                                   column=1)
    contador += 1

# Generar items bebidas
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0
for bebida in lista_bebidas:

    # Crear checkbuttons
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 15, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebidas[contador],
                         command=revisar_check)
    # Ubicar los checkbuttons dentro del respectivo panel
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                      font=('Dosis', 15, 'bold'),
                                      bd=1,
                                      width=4,
                                      state=DISABLED,
                                      textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=[contador],
                                   column=1)
    contador += 1

# Generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:

    # Crear checkbuttons
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 15, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postres[contador],
                         command=revisar_check)
    # Ubicar los checkbuttons dentro del respectivo panel
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # Crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Dosis', 15, 'bold'),
                                      bd=1,
                                      width=4,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=[contador],
                                   column=1)
    contador += 1

# Variables
var_precio_comida = StringVar()
var_precio_bebida = StringVar()
var_precio_postre = StringVar()
var_subtotal = StringVar()
var_iva = StringVar()
var_total = StringVar()
# Etiquetas de costos y campos de entrada
etiqueta_costo_comida = Label(panel_precios,
                              text='Precio plato:',
                              font=('Dosis', 10, 'bold'),
                              bg='burlywood4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_precio_comida = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_comida)
texto_precio_comida.grid(row=0, column=1, padx=50)

etiqueta_costo_bebida = Label(panel_precios,
                              text='Precio bebida:',
                              font=('Dosis', 10, 'bold'),
                              bg='burlywood4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_precio_bebida = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_bebida)
texto_precio_bebida.grid(row=1, column=1, padx=50)

etiqueta_costo_postre = Label(panel_precios,
                              text='Precio postre:',
                              font=('Dosis', 10, 'bold'),
                              bg='burlywood4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)

texto_precio_postre = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_precio_postre)
texto_precio_postre.grid(row=2, column=1, padx=50)

etiqueta_subtotal = Label(panel_precios,
                              text='Subtotal:',
                              font=('Dosis', 10, 'bold'),
                              bg='burlywood4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=50)

etiqueta_iva = Label(panel_precios,
                              text='Iva:',
                              font=('Dosis', 10, 'bold'),
                              bg='burlywood4',
                              fg='white')
etiqueta_iva.grid(row=1, column=2)

texto_iva = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_iva)
texto_iva.grid(row=1, column=3, padx=50)

etiqueta_total = Label(panel_precios,
                              text='Total:',
                              font=('Dosis', 10, 'bold'),
                              bg='burlywood4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_precios,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_total)
texto_total.grid(row=2, column=3, padx=50)

# Botones
lista_botones = ['total', 'factura', 'save', 'reset']
botones_creados = []

columna = 0
for boton in lista_botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 10, 'bold'),  # Cambié el tamaño de la fuente
                   fg='black',
                   bg='azure3',
                   bd=1,
                   width=6,  # Aumenté el ancho de los botones
                   padx=2,  # Añadí relleno horizontal
                   pady=5)  # Añadí relleno vertical
    botones_creados.append(boton)

    boton.grid(row=0, column=columna, padx=1, pady=2)  # Añadí espacio entre columnas
    columna += 1

botones_creados[0].config(command= total)
botones_creados[1].config(command= generar_factura)
botones_creados[2].config(command= guardar)
botones_creados[3].config(command= reset)

# Area de la factura
texto_factura = Text(panel_recibo,
                     font=('Dosis', 10, 'bold'),
                     bd=1,
                     width=32,
                     height=15)
texto_factura.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 15, 'bold'),
                          width=21,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', '*', 'R', 'B', '0', '/']
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 10, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=6)
    botones_guardados.append(boton)
    boton.grid(row= fila, column= columna)
    if columna == 3:
        fila += 1

    columna += 1
    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

# Evitar que la pantalla se cierre
aplicacion.mainloop()