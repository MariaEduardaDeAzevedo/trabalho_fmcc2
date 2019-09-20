#coding: utf-8

codon = input().upper()
p_adic = ""
parametros = list()

for n in codon:

    if n == "C":
        
        parametros.append(1)
        p_adic += "1"
    
    elif n == "A":
        
        parametros.append(2)
        p_adic += "2"

    elif n == "T" or n == "U":
        
        parametros.append(3)
        p_adic += "3"

    elif n == "G":

        parametros.append(4)
        p_adic += "4"

numero = 0
expo = 0

for a in parametros:
    
    numero += a*pow(5, expo)
    expo += 1

print(numero, p_adic, codon)

