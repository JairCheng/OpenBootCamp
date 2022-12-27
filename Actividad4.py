# Universitry Work

loop = "y"

# Menu: se hizo este display de menu por pedido del cliente

print("""
                                                 Bienvenido al Restaurante ZD!

                                                               Menu                                           

Lunes               | Martes           | Miercoles        | Jueves         | Viernes        | Sabado        | Domingo
Arroz               | Arroz frito      | Pure de Papa     | Pan Tostado    | Patacon        | Yuca Frita    | Papas Fritas
Pollo Asado         | Pollo Asado      | Batido de fruta  | Huevo Frito    | Higado         | Pollo Asado    | Pescado Apanado
Costilla agridulce  | Jugo de Naranja  | Pescado Apanado  | Cafe           | Carne frito    | Costilla      | Pollo Apanado
Ensalada de Papa    | Puerco Asado     | Pollo Apanado    | Bacon          | Bola de Carne  | Soda          | Ensalada
Lenteja             | Hoja de Mostaza  | Ensalada         | Chorizo        | Pasta          | Poroto        | Soda
Sopa de Pollo       | Poroto           | Tortilla         | Sopa especial  | Pizza          | Ensalada      | Shake
Holjadra            | Camaron          | Hamburguesa      | Bubble Tea     | Cafe           | Papa asado    | Hamburguesa


""")

#Se separa la lista en varias partes para evitar confusion

lunes_menu = ["Arroz", "Pollo Asado", "Costilla agridulce", "Ensalada de Papa", "Lenteja", "Sopa de Pollo", "Holjadra"]
lunes_precio = [1.00, 1.50, 2.00, 1.00, 1.00, 1.20, 0.30]

martes_menu = ["Arroz frito", "Pollo Asado", "Jugo de Naranja", "Puerco Asado", "Hoja de Mostaza", "Poroto", "Camaron"]
martes_precio = [1.50, 1.50, 0.80, 2.00, 1.00, 1.20, 3.00]

miercoles_menu = ["Pure de Papa", "Batido de fruta", "Pescado Apanado", "Pollo Apanado", "Ensalada", "Tortilla", "Hamburguesa"]
miercoles_precio = [1.50, 1.50, 0.80, 2.00, 1.00, 1.20, 3.00]

jueves_menu = ["Pan Tostado", "Huevo Frito", "Cafe", "Bacon", "Chorizo", "Sopa especial", "Bubble Tea"]
jueves_precio = [1.50, 1.50, 0.80, 2.00, 1.00, 1.20, 3.00]

viernes_menu = ["Patacon", "Higado", "Carne frito", "Bola de Carne", "Pasta", "Pizza", "Cafe"]
viernes_precio = [1.50, 1.50, 0.80, 2.00, 1.00, 1.20, 3.00]

sabado_menu = ["Yuca Frita", "Pollo Asado", "Costilla", "Soda", "Poroto", "Ensalada", "Papa asado"]
sabado_precio = [1.50, 1.50, 0.80, 2.00, 1.00, 1.20, 3.00]

domingo_menu = ["Papas Fritas", "Pescado Apanado", "Pollo Apanado", "Ensalada", "Soda", "Shake", "Hamburguesa"]
domingo_precio = [1.50, 1.50, 0.80, 2.00, 1.00, 1.20, 3.00]

semana_menu = [lunes_menu, martes_menu, miercoles_menu, jueves_menu, viernes_menu, sabado_menu, domingo_menu]
semana_precio = [lunes_precio, martes_precio, miercoles_precio, jueves_precio, viernes_precio, sabado_precio, domingo_precio]


#Se separa las funciones en 2 partes para evitar confusion al leer el codigo
def DisplayPrecio(MenuDia):
    MenuDia -= 1
    i = 0
    for x in semana_menu[MenuDia]:
        while i < 6:
            print("[", i + 1, "]",x, ": $", semana_precio[MenuDia][i])
            i += 1
            break

def Pedido(MenuDia):
    MenuDia -= 1
    Floop = "y"
    global total
    total = 0
    while Floop == "y":
        i = input("Seleccione la comida que desea: ")
        if float(i) > 0 and float(i) <= 6:
            total = total + semana_precio[MenuDia][int(i)-1]
            Floop = input("Desea pedir otra comida? y/n: ")
            Floop = Floop.lower()
            if Floop == "n":
                break
        else:
            print("Porfavor inserter una comida valida del menu del 1 al 6.")
            Floop = input("Desea regresar a insertar una comida valida? y/n: ")
            Floop = Floop.lower()
        

dia = input("Seleccione del 1 al 7 correspondiendo al dia de la semana: ")


if float(dia) > 0 and float(dia) <= 7:
    DisplayPrecio(int(dia))
    Pedido(int(dia))
    print("El total es: $", total)
else:
    print("Porfavor inserter un dia valido de la semana del 1 al 7.")
    loop = input("Desea regresar a insertar un dia valido? y/n: ")
    loop = loop.lower()


print("Muchas gracias por escoger a nosotros!")
