import math


class deber:
    #¿De cuál tipo de dato sería la variable donde almacena lo siguiente?
    #def ejercicio1(self)
    def ejercicio1(self):   
     pass
    #Dados dos (2) números calcule la suma, resta, multiplicación, división y módulo.
    def ejercicio4(self,num1,num2):
         sum=num1+num2
         res=num1-num2
         mul=num1*num2
         div=num1/num2
         rec=num1%num2
         print("{}+{}={}".format(num1,num2,sum))
         print("{}-{}={}".format(num1,num2,res))
         print("{}*{}={}".format(num1,num2,mul))
         print("{}/{}={}".format(num1,num2,div))
         print("{}%{}={}".format(num1,num2,rec))
         
    #Dados tres (3) números, Hacer una aplicación que calcule la resolvente
    # x2 - 9x + 8 = 0
    #int("Los coeficientes son: a = 1 ; b = -9  c = 8")
    #int(-b+-(b**2- 4ac//2a))
    #resultado= (x2 - 9x + 8 = 0)
    def ejercicio5(self):
        a=int(input("Ingrese a "))
        b=int(input("Ingrese b "))
        c=int(input("Ingrese c "))
        d = b**2-4*a*c
        if d < 0:
            print("NO existe Solucion")
        elif d == 0:
            x = (-b+math.sqrt(b**2-4*a*c))/2*a
            print("Tiene una unica solucion: ", x)
        else:
            x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
            x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
            print("Tiene dos soluciones: ", x1, " y", x2)   
     #Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.
    def ejercicio6(self):
         import math
         cateto1 = float(input("Introducir el Primer cateto: "))
         cateto2 = float(input("Introducir el Segundo cateto: "))
         print("La hipotenusa es: ")
         hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
         resultado = round ( hipotenusa, 2)
         print(resultado)   
     #Dado un (1) número, imprimir 0 si es par y 1 si es impar.
    def ejercicio7(self):
         num = input("Introduce un número: ")
         num = int(num)
         if num%2 == 0:
          print ("Este numero es 0")
         else:
            print ("Este numero es 1")        
        #dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. El bit
        #de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.
    def ejercicio9(self):
        binario=int(input("ingrese numero binario de 4 digitos: "))
        binario=str(binario)
        c=0
        for i in binario:
            if i in "1":
                c+=1
        if c%2==0:
            print('Su bit da paridad')
        else:
            print("Su bit no da paridad!")  
     #Dado un (1) número binario de cuatro (4) dígitos imprimir su valor   
    def ejercicio10(self):
        numero_binario = input("Introduce un número: ")
        numero_decimal = 0
        for posicion, digito_string in enumerate(numero_binario[::-1]):
    	     numero_decimal += int(digito_string) * 2 ** posicion
        print(numero_decimal)
        pass  
     #Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
     #decenas, centenas y unidades de mil.     
    def ejercicio11(self):
        numero = int(input("ingrese el numero: "))
        unimiel=(numero%10000-numero%1000)//1000
        centenas=(numero%1000-numero%100)//100
        decenas=(numero%100-numero%10)//10
        unidades=numero%10
        print ("unidad: " + repr (unidades))
        print ("decenas: " + repr (decenas))
        print ("centena: " + repr (centenas))
        print ("unidad de miel: " + repr (unimiel))
        print ()    
tarea = deber()
#tarea.ejercicio1()
# n1 = int(input("ingrese numero1=> "))
# n2 = int(input("ingrese numero2=> "))
# tarea.ejercicio4(n1,n2)
#tarea.ejercicio5()
#tarea.ejercicio6()
#tarea.ejercicio7()
#tarea.ejercicio9()
#tarea.ejercicio10()
#tarea.ejercicio11()
         
