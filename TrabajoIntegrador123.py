"""Ejercicio 1— “Caja del Kiosco”
Objetivo: Simular una compra con validaciones y cálculo de total.
Requisitos

1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
2. Pedir cantidad de productos a comprar (número entero positivo, validar con
.isdigit() en while).
3. Por cada producto (usar for):
o Pedir precio (entero, validar .isdigit()).
o Pedir si tiene descuento S/N (validar con while, aceptar s o n en
cualquier mayuscula/minuscula).
o Si tiene descuento: aplicar 10% al precio de ese producto.
4. Al final mostrar:
o Total sin descuentos
o Total con descuentos
o Ahorro total
o Promedio por producto (usar float y formatear con :.2f, ejem:
x = 3.14159
print(f"{x:.2f}"))
Validaciones obligatorias
• Sin try/except.
• No aceptar vacío en nombre (si queda vacío, es error).
• Cantidad > 0 (si ingresa 0, volver a pedir).
Salida esperada (ejemplo)
Cliente: Ana
Cantidad de productos: 3
Producto 1 - Precio: 100 Descuento (S/N): s
Producto 2 - Precio: 50 Descuento (S/N): n
Producto 3 - Precio: 200 Descuento (S/N): s
Total sin descuentos: $350
Total con descuentos: $320.00
Ahorro: $30.00
Promedio por producto: $106.67"""

'''
total_sin_descuento = 0
total_con_descuento = 0
total_ahorrado = 0

print("Buenos dias!")
while True:
    print("---------------------------------")
    nombre = input("Por favor, ingrese solo su nombre: ").capitalize().strip()
    if (nombre.replace(" ", "").isalpha() and nombre != ""):
        print(f"Bienvenido, {nombre}!")
        break
    else:
        print("El nombre ingresado no es valido. Intentelo de nuevo")
        continue
while True:
    print("---------------------------------")
    cant_prod = input("¿Cuantos productos desea comprar?: ")
    if (cant_prod.isdigit() and int(cant_prod) > 0):
        cant_prod = int(cant_prod)
        print(f"Cantidad ingresada: {cant_prod}")
        break
    else:
        print("La cantidad ingresada es invalida. Intente de nuevo.")
        continue
for i in range (cant_prod):
    while True:
        print("---------------------------------")
        precio_prod = input(f"Ingrese el precio del producto {i + 1}: ")
        if (precio_prod.replace(".","").isdigit() and precio_prod != "" and float(precio_prod) > 0):
            precio_prod = float(precio_prod)
            total_sin_descuento += precio_prod
            print("Precio Ingresado!")
            break 
        else:
            print("Valor ingresado invalido. Intentelo de nuevo.")
            continue
    while True:
        print("---------------------------------")
        descuento = input(f"¿Este producto esta en descuento? (S / N): ").upper().strip()
        match descuento:
            case "S":
                precio_desc = precio_prod * 0.90
                total_con_descuento += precio_desc
                print(f"Descuento del 10% aplicado!")
                break
            case "N":
                print("No se aplican descuentos.")
                total_con_descuento += precio_prod
                break
            case _:
                print("Dato Invalido. Intentelo de nuevo.")
total_ahorrado = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cant_prod
print("---------------------------------")
print(f"""El total sin descuentos seria de ${total_sin_descuento:.2f}!
      El total con descuentos seria de ${total_con_descuento:.2f}!
      El total ahorrado es de ${total_ahorrado:.2f}!
      El promedio por producto es de ${promedio:.2f}!""")
'''



"""Ejercicio 2 — “Acceso al Campus y Menú Seguro”
Objetivo: Login con intentos + menú de acciones con validación estricta.
Requisitos
1. Definir credenciales fijas en el código:
o usuario correcto: "alumno"
o clave correcta: "python123"
2. Permitir máximo 3 intentos para ingresar usuario y clave.
3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
1. Ver estado de inscripción (mostrar “Inscripto”)
2. Cambiar clave (pedir nueva clave y confirmación; deben
coincidir)
3. Mostrar mensaje motivacional (1 frase)
4. Salir
5. Validación del menú:
o Debe ser número (.isdigit())
o Debe estar entre 1 y 4
Cambio de clave
• La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no,
rechazar.
Salida esperada
Intento 1/3 - Usuario: alumno
Clave: xxx
Error: credenciales inválidas.
Intento 2/3 - Usuario: alumno
Clave: python123
Acceso concedido.
1) Estado 2) Cambiar clave 3) Mensaje 4) Salir
Opción: a
Error: ingrese un número válido.
Opción: 5
Error: opción fuera de rango.
Opción: 2
Nueva clave: 123
Error: mínimo 6 caracteres."""

'''usuario_correcto = "alumno"
contraseña_correcta = "python123"
intentos = 1
mensajes = ["Tu imaginación puede llevarte a lugares maravillosos.", "Cada día es una nueva oportunidad para aprender algo increíble.", "No tengas miedo de intentar, ahí empieza la magia."]
import random
while True:
    print("------------------------")
    if intentos == 4:
        print("SE HA ALCANZADO EL LIMITE DE INTENTOS. CUENTA BLOQUEADA Y SALIENDO DEL PROGRAMA...")
        break
    print("Por favor, ingrese sus credenciales a continuación:")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if (usuario != usuario_correcto or contraseña != contraseña_correcta):
        print(f"Usuario y/o contraseña incorrectos. Intente de nuevo (Intento {intentos}/3)")
        intentos += 1
        continue
    else:
        print("------------------------")
        print("Se ha acccedido como 'alumno'!")
        while True:
            print("""------------------------
MENU - CAMPUS VIRTUAL
Seleccione una de las siguientes opciones:                
                  1 - Ver estado de Inscripción
                  2 - Cambiar clave
                  3 - Mostrar mensaje motivacional
                  4 - Salir
                  """)
            opciones = input("               -->")
            if not opciones.isdigit():
                print("Dato Ingresado invalido. Intente de nuevo") 
                continue
            else:
                opciones = int(opciones)
                match opciones:
                    case 1:
                        print("Usted esta Inscripto!")
                        continue
                    case 2:
                        nueva_contraseña = input("Ingrese su nueva contraseña (Debe tener al menos 6 caracteres): ")
                        confirmación = input("Confirme su nueva contraseña: ")
                        if nueva_contraseña != confirmación:
                            print("La nueva contraseña no coincide con la confirmación. Intentelo de nuevo.")
                            continue
                        elif nueva_contraseña == contraseña_correcta:
                            print("La nueva contraseña no puede ser igual a la anterior. Intentelo de nuevo.")
                            continue
                        elif len(nueva_contraseña) < 6:
                            print("La contraseña no puede tener menos de 6 caracteres. Intente de nuevo.")
                            continue
                        else:
                            contraseña_correcta = nueva_contraseña
                            print("La contraseña ha sido cambiada con exito!")
                            continue
                    case 3:
                        mensaje = random.randint(0,2)
                        print(mensajes[mensaje])
                        continue
                    case 4:
                        print("Saliendo del menu.")
                        intentos = 1
                        break
                    case _:
                        print("Entrada invalida. Intente de nuevo")
                        continue
'''


"""Contexto
Hay 2 días de atención: Lunes y Martes.
Cada día tiene cupos fijos:
• Lunes: 4 turnos
• Martes: 3 turnos
Reglas
1. Pedir nombre del operador (solo letras).
2. Menú repetitivo hasta salir:
1. Reservar turno
2. Cancelar turno (por nombre)
3. Ver agenda del día
4. Ver resumen general
5. Cerrar sistema
3. Reservar:
o Elegir día (1=Lunes, 2=Martes).
o Pedir nombre del paciente (solo letras).
o Verificar que no esté repetido en ese día (comparando con las variables
ya cargadas).
o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
4. Cancelar:
o Elegir día.
o Pedir nombre del paciente (solo letras).
o Si existe, cancelar y dejar el espacio vacío ("").
5. Ver agenda del día:
o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si
está vacío.
6. Resumen general:
o Turnos ocupados y disponibles por día.
o Día con más turnos (o empate).
Restricciones
• ❌ No listas, no diccionarios, no sets, no tuplas.
• ✅ Se permite usar "" como “vacío”.
• ✅ Validaciones con .isalpha() y .isdigit() (sin try/except)"""

'''lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    operador = input("Ingrese su nombre de operador: ")
    if operador.isalpha():
        print(f"Bienvenido {operador}!")
        break
    else:
        print("Error: El nombre solo puede contener letras. Intente de nuevo.")
        continue
while True:
    print("""----------------
          MENU PRINCIPAL
          1 - Agendar Turno
          2 - Cancelar Turno
          3 - Ver agenda del día
          4 - Ver resumen general
          5 - Salir""")
    opciones = input("Seleccione una de las opciones anteriores: ")
    match opciones:
        case "1":
            dia = input("Seleccione el dia a reservar (1-Lunes; 2-Martes): ")
            if not dia.isdigit() or dia not in ["1", "2"]:
                print("Error: Debe ingresar 1 (Lunes) o 2 (Martes). Intentelo de nuevo.")
                continue
            paciente = input("Ingrese el nombre del paciente: ").strip()
            if not paciente.isalpha():
                print("Error: El nombre solo puede contener letras. intentelo de nuevo.")
                continue
            if dia == "1":
                if paciente in [lunes1, lunes2, lunes3, lunes4]:
                    print("Error: Ese paciente ya tiene turno el lunes.")
                    continue
                elif lunes1 == "":
                    lunes1 = paciente
                    print("Turno reservado en Lunes (Turno 1)")
                    continue
                elif lunes2 == "":
                    lunes2 = paciente
                    print("Turno reservado en Lunes (Turno 2)")
                    continue
                elif lunes3 == "":
                    lunes3 = paciente
                    print("Turno reservado en Lunes (Turno 3)")
                    continue
                elif lunes4 == "":
                    lunes4 = paciente
                    print("Turno reservado en Lunes (Turno 4)")
                    continue
                else:
                    print("No quedan turnos disponibles para el lunes.")
                    continue
            elif dia == "2":
                if paciente in [martes1, martes2, martes3]:
                    print("Error: Ese paciente ya tiene turno el martes.")
                    continue
                elif martes1 == "":
                    martes1 = paciente
                    print("Turno reservado en Martes (Turno 1)")
                    continue
                elif martes2 == "":
                    martes2 = paciente
                    print("Turno reservado en Martes (Turno 2)")
                    continue
                elif martes3 == "":
                    martes3 = paciente
                    print("Turno reservado en Martes (Turno 3)")
                    continue
                else:
                    print("No quedan turnos disponibles para el Martes.")
                    continue
        case "2":
            dia = input("Seleccione el dia a para cancelar la reserva (1-Lunes; 2-Martes): ")
            if not dia.isdigit() or dia not in ["1", "2"]:
                print("Error: Debe ingresar 1 (Lunes) o 2 (Martes). Intentelo de nuevo.")
                continue
            paciente = input("Ingrese el nombre del paciente: ").strip()
            if not paciente.isalpha():
                print("Error: El nombre solo puede contener letras. intentelo de nuevo.")
                continue
            if dia == "1":
                if paciente == lunes1:
                    lunes1 = ""
                    print("Se ha cancelado el turno!")
                    continue
                elif paciente == lunes2:
                    lunes2 = ""
                    print("Se ha cancelado el turno!")
                    continue
                elif paciente == lunes3:
                    lunes3 = ""
                    print("Se ha cancelado el turno!")
                    continue
                elif paciente == lunes4:
                    lunes4 = ""
                    print("Se ha cancelado el turno!")
                    continue
                else:
                    print("El paciente no tiene turnos reservados para el Lunes.")
                    continue
            elif dia == "2":
                if paciente == martes1:
                    martes1 = ""
                    print("Se ha cancelado el turno!")
                    continue
                elif paciente == martes2:
                    martes2 = ""
                    print("Se ha cancelado el turno!")
                    continue
                elif paciente == martes3:
                    martes3 = ""
                    print("Se ha cancelado el turno!")
                    continue
                else:
                    print("El paciente no tiene turnos reservados para el Martes.")
                    continue
        case 3:
            dia = input("Selecciona el dia para ver la agenda (1-Lunes; 2-Martes): ")
            if not dia.isdigit() or dia not in ["1", "2"]:
                print("Error: Debe ingresar 1 (Lunes) o 2 (Martes). Intentelo de nuevo.")
                continue
            if dia == "1":
                print(f"""Agenda del dia lunes:
                      Turno 1: {lunes1 if lunes1 != "" else "libre"} 
                      Turno 2: {lunes2 if lunes2 != "" else "libre"}
                      Turno 3: {lunes3 if lunes3 != "" else "libre"}
                      Turno 4: {lunes4 if lunes4 != "" else "libre"}""")
                continue
            elif dia == "2":
                print(f"""Agenda del dia martes:
                      Turno 1: {martes1 if martes1 != "" else "libre"}
                      Turno 2: {martes2 if martes2 != "" else "libre"}
                      Turno 3: {martes3 if martes3 != "" else "libre"}""")
                continue
        case "4":
            ocupados_lunes = 0
            if lunes1 != "":
                ocupados_lunes += 1
            if lunes2 != "":
                ocupados_lunes += 1
            if lunes3 != "":
                ocupados_lunes += 1
            if lunes4 != "":
                ocupados_lunes += 1
            libres_lunes = 4 - ocupados_lunes
            ocupados_martes = 0
            if martes1 != "":
                ocupados_martes += 1
            if martes2 != "":
                ocupados_martes += 1
            if martes3 != "":
                ocupados_martes += 1
            libres_martes = 3 - ocupados_martes
            print(f"""Resumen general:
                  Lunes: {ocupados_lunes} ocupados, {libres_lunes} libres
                  Martes: {ocupados_martes} ocupados, {libres_martes} libres""")
            if ocupados_lunes > ocupados_martes:
                print("El dia mas ocupado es el dia Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("El dia mas ocupado es el dia Martes")
            else:
                print(f"Ambos dias estan igual de ocupados ({ocupados_martes} turnos ocupados).")
            continue
        case "5":
            print("Saliendo...")
            break
        case _:
            print("Entrada invalida. Intentelo de nuevo.")
            continue'''
'''Ejercicio 4: Escape Room - La Boveda'''

'''energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0
while True:
    nombre_agente = input("Ingrese su nombre de agente: ")
    if nombre_agente.isalpha():
        if nombre_agente.capitalize() == "Duende tuneado":
            print("Bienvenido... Administrador...")
            break
        else:
            print(f"Bienvenido, agente {nombre_agente}")
            break
    else:
        print("Error: El nombre no es valido. Solo puede contener letras. Intentelo de nuevo.")
        continue
print("------------------------------")
print("""ATENCIÓN: Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
limitados.
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.""")
continua = True
while continua == True:
    if energia <= 0:
        print("Has perdido por quedarte sin energía. La bóveda sigue cerrada.")
        break
    elif tiempo <= 0:
        print("Has perdido por quedarte sin tiempo. La bóveda sigue cerrada.")
        break
    elif cerraduras_abiertas == 3:
        print("¡Felicidades! Has abierto las 3 cerraduras y ganado el juego.")
        break
    elif alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Has perdido por que la alarma se ha activado y no te queda tiempo para abrir las cerraduras restantes. La bóveda sigue cerrada.")
        break
    print("------------------------------")
    print(f"Energía: {energia} | Tiempo: {tiempo} | cerraduras abiertas: {cerraduras_abiertas}")
    print("""Selecciona un movimiento:
          (1)- Forzar cerradura (costo: -20 energía, -2 tiempo)
          (2)- Hackear panel (costo: -10 energía, -3 tiempo)
          (3)- Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)""")
    movimiento = input("Seleccione 1, 2 o 3 segun el movimiento que desea realizar: ").strip()
    if movimiento.isalpha():
        print("Error: La entrada no es valida. Debe ingresar un numero (1, 2 o 3). Intentelo de nuevo.")
        continue
    elif movimiento.isdigit():
        movimiento = int(movimiento)
        if movimiento <= 0 or movimiento > 3:
            print("Error: La entrada no es valida. Debe ingresar 1, 2 o 3. Intentelo de nuevo.")
            continue
        else:
            match movimiento:
                case 1:
                    energia -= 20
                    tiempo -= 2
                    forzar_seguidas += 1
                    if energia < 40:
                        while True:
                            print("Peligro: Riesgo de alarma")
                            riesgo = input("Ingrese un numero del 1-3: ").strip()
                            if riesgo.isalpha():
                                print("Error: La entrada no es valida. Debe ingresar un numero (1, 2 o 3). Intentelo de nuevo.")
                                continue
                            elif riesgo.isdigit():
                                riesgo = int(riesgo)
                                if riesgo == 3:
                                    alarma = True
                                    print("¡La alarma ha sido activada y la cerradura se ha bloqueado!")
                                    break
                                else:
                                    print("¡Has logrado forzar la cerradura sin activar la alarma!")
                                    cerraduras_abiertas += 1
                                    break
                    elif forzar_seguidas == 3:
                        print("Has intentado forzar la cerradura 3 veces seguidas. ¡La alarma se ha activado y la cerradura se ha bloqueado!")
                        alarma = True
                        forzar_seguidas = 0
                        continue
                    else:
                        print("Has forzado una cerradura con exito!")
                        cerraduras_abiertas += 1
                        continue
                case 2:  
                    energia -= 10
                    tiempo -= 3
                    forzar_seguidas = 0 
                    for i in range(4):
                        codigo_parcial += "A"
                        print(f"Hackeando paso {i+1}... Código parcial: {codigo_parcial}")
                    if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                        cerraduras_abiertas += 1
                        print("¡Has hackeado el panel y abierto una cerradura!")
                    else:
                        print(f"Progreso actual del código: {codigo_parcial}")
                case 3:  
                    energia += 15
                    if energia > 100:
                        energia = 100
                    tiempo -= 1
                    if alarma:
                        energia -= 10
                        print("Descansaste, pero la alarma activa drenó energía extra.")
                    else:
                        print("Has descansado y recuperado energía.")
                    forzar_seguidas = 0
'''

'''Ejercicio 5: Escape Room - La Arena del Gladiador'''

'''while True:
    nombre_gladiador = input("Nombre del Gladiador: ").strip()
    if nombre_gladiador.isalpha():
        break
    elif nombre_gladiador.capitalize() == "Duende tuneado":
        print(f"Nos volvemos a encontrar... {nombre_gladiador}")
    else:
        print("Error: Solo se permiten letras.")

print("=== INICIO DEL COMBATE ===")

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True

while vida_gladiador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        while True:
            opcion = input("Opción: ").strip()
            if not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                continue
            opcion = int(opcion)
            if opcion < 1 or opcion > 3:
                print("Error: Debe elegir 1, 2 o 3.")
                continue
            break

        if opcion == 1:
            if vida_enemigo < 20:
                daño = ataque_pesado * 1.5
                print(f"¡Golpe Crítico! Atacaste al enemigo por {daño} puntos de daño!")
            else:
                daño = ataque_pesado
                print(f"¡Atacaste al enemigo por {daño} puntos de daño!")
            vida_enemigo -= int(daño)

        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == 3:
            if pociones > 0:
                vida_gladiador += 30
                pociones -= 1
                print(f"¡Has usado una poción! Recuperaste 30 HP. Pociones restantes: {pociones}")
            else:
                print("¡No quedan pociones!")

        vida_gladiador -= ataque_enemigo
        print(f">> ¡El enemigo contraataca por {ataque_enemigo} puntos!")

    turno_gladiador = True

print("=== FIN DEL COMBATE ===")
if vida_gladiador > 0 and vida_enemigo <= 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
elif vida_gladiador <= 0:
    print("DERROTA. Has caído en combate.")'''