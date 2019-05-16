# -*- coding: utf-8 -*-
#import pandas as pd
#import secrets
#from phe import paillier
#from pyprimes import isprime

class colegi():
    def __init__(self, nom_colegi, Kpublica_censo):
        self.nom_colegi = nom_colegi
        self.Kpublica_censo = Kpublica_censo
        self.kpublica_mesa_electoral = self.get_kpublica_mesa_electoral()
        self.lista_votos = []
    def validar_votante(self, certificado_votante):
        validez = False        
        e, n = self.Kpublica_censo.return_variables()
        msg = pow(int(certificado_votante["k_pub_firmada_censo"]), int(e), int(n))        
        if msg == int(certificado_votante["k_pub_votante"]):
            validez = True
        
        return validez

    def get_kpublica_mesa_electoral(self):
        return "hello"
    def send_results(self):
        return "hello"
    def votar(self):
        return "hello"