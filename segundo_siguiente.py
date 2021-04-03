"""
Tarea: Tarea 16: siguiente segundo
Author: Samuel Alejandro Pérez
Fecha de entrega: 25/03/21
Grupo: ESI-232A4
Profesor: Jorge Zaldivar
Este programa calcula el siguiente segundo de una hora determinada por el usuario.
"""
# Entradas
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
# Proceso
if (horas == 23 and segundos == 59 and minutos ==59) :
# No se porque pero en esta linea, si le dejo que segundos es igual a segundos - 59 me da como resultado 1, asi que le puse 60.
 segundos -= 60
 minutos -= 59
 horas = 0
if segundos < 59:
 segundos += 1
if (segundos == 59 and minutos ==59):
 segundos = segundos - 59
 minutos -= 59
 horas += 1
if segundos == 59:
 segundos = segundos - 59
 minutos += 1
# Salidas
print()
print("Hora final")
print(horas,"h", minutos,"m", segundos,"s")
