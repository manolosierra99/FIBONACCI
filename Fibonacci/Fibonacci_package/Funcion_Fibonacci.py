'''
Created on 23 nov. 2016

@author: Manuel
'''
def Fibonacci(numero):
    if numero==1:
        return 1
    if numero==0:
        return 0
    else:
        return Fibonacci(numero-1)+Fibonacci(numero-2)
if __name__ =="__main__":
    numero=int(input("Escribe un numero sobre el que desea saber su ecuacion de Fibonacci:"))
    print(Fibonacci(numero))
