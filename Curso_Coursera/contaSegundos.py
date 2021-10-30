segundos = int(input("Por favor, entre com o número de segundos que deseja converter:"))
dias = segundos // 86400
dias_restantes = segundos % 86400
horas = dias_restantes // 3600
horas_restantes = dias_restantes % 3600
minutos = horas_restantes // 60
minutos_restantes = segundos % 60

print( dias, "dias,", horas, "horas,", minutos, "minutos e", minutos_restantes, "segundos")