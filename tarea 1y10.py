class deber:
#ESTRUCTURA DE CONTROLDE FLUJO DE DATOS.
#Todos los años que se dividen exactamente entre 400, o que son divisibles 
#exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos. 
#Usando estas premisas crea un algoritmo que lea una fecha como un número 
#entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si 
#el mismo es un año bisiesto o no.
 def ejercicio1(self):
     print('Determina si un año es bisiesto')
     a=int(input("Introduce el año: "))
     if a%4==0 and a%100!=0 or a%400==0:
      print(a," es un año bisiesto")
     else:
      print(a," no es un año bisiesto")
      
#Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es capicúa.
 def ejercicio2(self):
     numero=int(input("ingrese un numero:"))
     centena=numero/100
     decena=(numero%100)/10
     unidad=(numero%100)%10

     if(centena==unidad):
        print("el numero es capiuca")
     else:
        print("el numero no es capiuca") 
        
#Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como resultado su equivalente en segundos.
 def ejercicio3(self):
    h=int(input("Ingresa hora\n"))
    m=int(input("Ingresa minuto\n"))

    hh=h*3600
    mm=m*60
    t=hh+mm
    print("los segundos son:")
    print(t)
#Para un valor entero positivo que representa una cantidad en segundos, indicar su equivalente en minutos, horas y días.
 def ejercicio4(self):
        segundos = int(input("ingrese los segundos"))
        dias = segundos // (20*60*60)
        segundos = segundos % (24*60*60)
        horas = segundos // (60*60)
        segundos = segundos % (24*60*60)
        minutos = segundos // 60
        print("dias:{} horas:{} minutos: {}".format(dias,horas,minutos))
#Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el mayor? y ¿cuál es el segundo mayor?        
 def ejercicio5(self):
        abc=['1','2','3']
        lista=[0]*3
        indice=0
        while indice<3:
            while lista[indice]<=0:
                lista[indice]=int(input(f"Ingrese numero {abc[0+indice]}: "))
            indice+=1
        ma=max(lista)
        mi=min(lista)
        if lista[0]==mi:
            del lista[0]
        elif lista[1]==mi:
            del lista[1]
        else:
            del lista[2]
        print(f"El numero mayor es: {max(lista)}")
        print(f"El segundo numero mayor es: {min(lista)}")
        
#a. Menor a 16: Criterio de ingreso.
#b. 16 a 16.9: infra peso.
#c. 17 a 18.4: bajo peso.
#d. 18.5 a 24.9: peso normal.
#e. 25 a 29.9: sobrepeso.
#f. 30 a 34.9: obesidad pre-mórbida.
#g. 40 a 45: obesidad mórbida.
#h. Mayor a 45: obesidad híper-mórbida.
 def ejercicio7(self):
     masa = float(input('Inserte su masa en kilogramos:'))
     estatura = float(input('Inserte su estatura en metros:'))
     imc = masa / estatura**2

     if imc < 16:
       print('Tiene delgadez severa')
     elif imc >=16 and imc < 17 :
       print('Tiene delgadez moderada')
     elif imc >=17 and imc < 18.5 :
       print('Tiene delgadez leve')
     elif imc >=18.5 and imc < 25 :
       print('Tiene IMC normal')
     elif imc >=25 and imc < 30 :
       print('Tiene preobesidad')
     elif imc >=30 and imc < 35 :
       print('Tiene obesidad leve')
     elif imc >=35 and imc < 40 :
       print('Tiene obesidad media')
     elif imc >= 40 :
       print('Tiene obesoidad morbida')
     else:
       print('Opcion invalida')

       print('Su imc fue de ', imc)      
#Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año 
#2014 e imprima por pantalla el número de días que han pasado desde el 1 de 
#Enero de 2014 hasta la fecha dada.
 def ejercicio8(self):
     if __name__ == '__main__':
         print("Ingrese Número del Mes (1 - 12) : ")
     num = int(input())
     if num==1:
          print("ENERO")
     elif num==2:
          print("FEBRERO")
     elif num==3:
          print("MARZO")
     elif num==4:
          print("ABRIL")
     elif num==5:
          print("MAYO")
     elif num==6:
          print("JUNIO")
     elif num==7:
          print("JULIO")
     elif num==8:
          print("AGOSTO")
     elif num==9:
          print("SETIEMBRE")
     elif num==10:
          print("OCTUBRE")
     elif num==11:
          print("NOVIEMBRE")
     elif num==12:
          print("DICIEMBRE")
     else:
          print("NÚMERO DEL MES INCORRECTO")       
#Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho 
#número.
 def ejercicio9(self):
     if __name__ == '__main__':
      print("Ingrese Número del Mes (1 - 12) : ")
      num = int(input())
     if num==1:
          print("ENERO")
     elif num==2:
          print("FEBRERO")
     elif num==3:
          print("MARZO")
     elif num==4:
          print("ABRIL")
     elif num==5:
          print("MAYO")
     elif num==6:
          print("JUNIO")
     elif num==7:
          print("JULIO")
     elif num==8:
          print("AGOSTO")
     elif num==9:
          print("SETIEMBRE")
     elif num==10:
          print("OCTUBRE")
     elif num==11:
          print("NOVIEMBRE")
     elif num==12:
          print("DICIEMBRE")
     else:
          print("NÚMERO DEL MES INCORRECTO")            
# En un almacén se hace un 20% de descuento a los clientes cuya compra supere
# los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
# pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
# necesario.
 def ejercicio10(self):
     
   if __name__ == '__main__':
     print("Ingrese Monto : ")
     monto = float(input())
     if monto>1000:
          print("Tendrá un Descuento del 20% : ",monto*0.20)     

         
tarea = deber()
#tarea.ejercicio1()
#tarea.ejercicio2()
#tarea.ejercicio3()
#tarea.ejercicio4()
#tarea.ejercicio5()
#tarea.ejercicio7()
#tarea.ejercicio8()
#tarea.ejercicio9()
#tarea.ejercicio10()
