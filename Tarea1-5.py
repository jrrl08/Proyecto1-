class deber:
# Construya una función que solicite edades al usuario y determine el promedio de
# las edades mayores a 18 años. El usuario indicará cuando desea dejar de
# suministrar datos de entrada. En la Acción Principal se informará el promedio
# calculado.
 def ejercicio1(self):
     acumulador = int(0)
     for x in range (1,5):
       edad = int(input("ingrese la edad: "))
       acumulador = acumulador + edad
     print("El promedio de las edades es: ", str(acumulador / 5))

# Construya una función “Eleva” Que reciba como parámetros una base y un
# exponente y retorne al algoritmo principal el resultado de elevar un numero al otro.
 def ejercicio2(self):
     base = int(input("Ingrese la base: "))
     exponente = int(input("Ingrese el exponente: "))
     potencia = base ** exponente
     print(str(base)+"^"+str(exponente)+" es igual a: ",potencia)
#Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la suma de los lados del polígono)    
 def ejercicio3(self):
        lado=float(input("Ingrese un lado del pentágono!:"))
        perimetro=5*lado
        print( perimetro)
# En una empresa pagan según las horas trabajadas y una tarifa fija por hora. Si la
# cantidad de horas trabajadas en una semana es mayor a 40, la tarifa se
# incrementa en un 35% para las horas extras. Escribe una acción principal que
# solicite la identificación de 5 empleados, el monto cancelado por hora, y la
# cantidad de horas trabajadas por cada uno, llame a acciones/funciones que
# calculen el salario semanal por horas trabajadas (<=40) y los ingresos por
# concepto de horas extras, y finalmente informe los resultados en la acción
# principal.
 def ejercicio4(self):
        def CalculaSalario(pagoHora, horas):
            pagoHora=int(pagoHora)
            horas=int(horas)
            conc=[]
            if horas>40:
                extra=horas-40
                Hnormal=horas-extra
                ph=Hnormal*pagoHora
                pe=(pagoHora*0.35+pagoHora)*extra
                totSemana=ph+pe
                horas*=pagoHora
                conc.append(totSemana),conc.append(ph),conc.append(pe)
            else:
                ph=pagoHora*horas
                conc.append(ph)
            return conc
        empleados=['']*15
        abc=['1','','','2','','','3','','','4','','','5']
        indice=0
        while indice<=14:
            if indice==0 or indice==3 or indice==6 or indice==9 or indice==12:
                while empleados[indice]<='':
                    empleados[indice]=input(f"Ingrese su identificacion Empleado {abc[0+indice]}: ")
                indice+=1
            elif indice==1 or indice==4 or indice==7 or indice==10 or indice==13:
                while empleados[indice]<='':
                    empleados[indice]=input(f"Ingrese el pago por hora: ")
                indice+=1
            else:
                while empleados[indice]<='':
                    empleados[indice]=input(f"Ingrese las horas trabajadas durante la semana: ")
                indice+=1
        conc=CalculaSalario(empleados[1], empleados[2])
        if len(conc)==3:
            print(f"{empleados[0]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin Horas extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[0]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[4], empleados[5])
        if len(conc)==3:
             print(f"{empleados[3]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[3]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[7], empleados[8])
        if len(conc)==3:
            print(f"{empleados[6]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[6]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[10], empleados[11])
        if len(conc)==3:
            print(f"{empleados[9]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[9]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
        conc=CalculaSalario(empleados[13], empleados[14])
        if len(conc)==3:
            print(f"{empleados[12]}:\nIngresos por horas extras: ${conc[2]}\nIngresos por horas trabajadas (sin H extras): ${conc[1]}\nIngreso total de la semana: ${conc[0]}\n")
        else:
            print(f"{empleados[12]}:\nNo realizo horas extras.\nIngreso total de la semana: ${conc[0]}\n")
# Escriba una acción (MillasAKilometros) que convierta una distancia en millas a
# kilómetros (1milla = 1.60935km). Esta acción recibirá como parámetros: el nombre
# de la ciudad origen, el nombre de la ciudad destino y la distancia en millas entre
# ellas y debe retornar la distancia entre las ciudades en kilómetros.
# Desarrolle además una acción principal en donde utilice a la acción
# MillasAKilometros para convertir e informar la distancia en kilómetros entre 4 pares
# de ciudades suministradas por el usuario.
 def ejercicio5(self):
        def MillasAKilometros(millas):
            kilom=millas*1.60935
            return kilom
        ciudades=['']*12
        abc=['A','B','','C','D','','F','G','','H','I']
        indice=0
        while indice<=11:
            if indice==0 or indice==1 or indice==3 or indice==4 or indice==6 or indice==7 or indice==9 or indice==10:
                while ciudades[indice]<='':
                    ciudades[indice]=input(f"Ingrese ciudad {abc[0+indice]}: ")
                indice+=1
            else:
                while ciudades[indice]<='':
                    ciudades[indice]=input(f"Ingrese distancia entre ciudades en millas: ")
                indice+=1
        print(f"\nEntre {ciudades[0]} y {ciudades[1]}, hay {MillasAKilometros(int(ciudades[2])):.2f} Km de distancia\n")
        print(f"Entre {ciudades[3]} y {ciudades[4]}, hay {MillasAKilometros(int(ciudades[5])):.2f} Km de distancia\n")
        print(f"Entre {ciudades[6]} y {ciudades[7]}, hay {MillasAKilometros(int(ciudades[8])):.2f} Km de distancia\n")
        print(f"Entre {ciudades[9]} y {ciudades[10]}, hay {MillasAKilometros(int(ciudades[11])):.2f} Km de distancia\n")

tarea = deber()
#tarea.ejercicio1()
#tarea.ejercicio2()
#tarea.ejercicio3()
#tarea.ejercicio4()
tarea.ejercicio5()