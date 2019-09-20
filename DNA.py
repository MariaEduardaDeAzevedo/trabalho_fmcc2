#coding: utf-8

from Codon import *

class DNA:

    def __init__(self):

        self.tripa = list()
        self.anti_tripa = list()

    def add_codon(self, a, b, c):
        
        codon = Codon(a.upper(), b.upper(), c.upper())
        self.tripa.append(codon)
        self.anti_tripa.append(codon.anti_codon())
    
    def get_codon(self, pos):

        if pos < len(self.tripa):

            return self.tripa[pos]

        return " "

    def get_tripa(self):

        return self.tripa
    
    def get_anti_tripa(self):

        return self.anti_tripa

    def get_anti_codon(self, pos):

        if pos < len(self.tripa):

            return self.tripa[pos].anti_codon()

        return " "

    def codigo(self):

        codigo = ""

        for i in range(0, len(self.tripa)):

            codigo += str(self.tripa[i].p_adic_numerico() + self.anti_tripa[i].p_adic_numerico())
            
        return int(codigo)
        
    def __str__(self):
        
        dupla_helice = ""

        for c in self.tripa:

            dupla_helice += c.__str__()

        dupla_helice += "\n"

        for i in range(0, len(self.tripa)):
            
            dupla_helice += "|" * 3    
        
        dupla_helice += "\n"

        for c in self.anti_tripa:

            dupla_helice += c.__str__()
        
        return dupla_helice
