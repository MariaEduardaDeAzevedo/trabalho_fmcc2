#coding: utf-8

class Codon:

    def __init__(self, n0, n1, n2):
        
        self.numeros = {"C": 1, "A":2, "T":3, "U":3, "G":4} 
        self.nucleotideos = [n0, n1, n2]
        self.anti_bases = {"C":"G", "G":"C", "T":"A", "A": "T"}

    def __str__(self):

        return "%s%s%s" % (self.nucleotideos[0], self.nucleotideos[1], self.nucleotideos[2])

    def p_adic_numerico(self):
        
        expo = 0
        p = 5
        p_adic = 0

        for n in self.nucleotideos:

            p_adic += self.numeros[n] * pow(p, expo)
            expo += 1
    
        return p_adic

    def p_adic_codigo(self):

        p_adic = ""

        for n in self.nucleotideos:

            p_adic += str(self.numeros[n])

        return int(p_adic)

    def anti_codon(self):
        
        anti = list()

        for n in self.nucleotideos:
            
            anti.append(self.anti_bases[n])
        
        return Codon(anti[0], anti[1], anti[2])


