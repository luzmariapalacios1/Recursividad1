__author__='LuzMaria'
Numero=7

def SumaPrimerosNumeros(Numero):
    if(Numero==1):
        return 1
    else:
        return Numero + SumaPrimerosNumeros(Numero - 1)

print('Numero a sumar:  ', Numero)
print('La suma de los primeros es:  ', (SumaPrimerosNumeros(Numero)))