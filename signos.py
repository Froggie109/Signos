#Hacer un programa que pida el día y mes de cumpleaños e indique cuál es su signo del Zodiaco.
dia = int(input("Escribir el día de nacimiento: "))
mes = input("Escribir el mes de nacimiento: ")

if (mes=="marzo" or mes=="abril"):
    if (dia>=1 and dia<=21):
        print("Signo: Aries.")
    elif (dia>=22 and dia<=30):
        print("Signo: Tauro.")
elif (mes=="mayo"):
    if (dia>=1 and dia<=20):
        print("Signo: Tauro.")
    elif (dia>=21 and dia<=31):
        print("Signo: Géminis.")
elif (mes=="junio"):
    if (dia>=1 and dia<=21):
        print("Signo: Géminis.")
    elif(dia>21 and dia <=30):
        print("Signo: Cáncer.")
elif (mes=="julio"):
    if (dia>=1 and dia <=23):
        print("Signo: Cáncer.")
    elif (dia>23 and dia <=31):
        print("Signo: Leo.")
elif (mes=="agosto"):
    if (dia>=1 and dia <=23):
        print("Signo: Leo.")
    elif (dia>23 and dia <=31):
        print("Signo: Virgo.")
elif (mes=="septiembre"):
    if (dia>=1 and dia <=22):
        print("Signo: Virgo.")
    elif(dia>22 and dia <=30):
        print("Signo: Libra.")
elif (mes =="octubre"):
    if (dia>=1 and dia <=23):
        print("Signo: Libra.")
    elif(dia>23 and dia <=31):
        print("Signo: Escorpio.")
elif (mes=="noviembre"):
    if (dia>=1 and dia <=22):
        print("Signo: Escorpio.")
    elif(dia>22 and dia <=30):
        print("Signo: Sagitario.")
elif (mes=="diciembre"):
    if (dia>=1 and dia <=23):
        print("Signo: Sagitario.")
    elif(dia>23 and dia <=31):
        print("Signo: Capricornio.")
elif (mes=="enero"):
    if (dia>=1 and dia <=23):
        print("Signo: Capricornio.")
    elif(dia>23 and dia <=31):
        print("Signo: Acuario.")
elif (mes=="febrero"):
    if (dia>=1 and dia <=19):
        print("Signo: Acuario.")
    elif(dia>19 and dia <=29):
        print("Signo: Piscis.")
else:
    print("No, así no funciona.")
            
