from abc import ABC,abstractmethod
import numpy as np
from operator import itemgetter
import random

## Esta es una clase generica para una busqueda local
class local(ABC):
    def __init__(self,grafo,gs):
        self.grafo=grafo
        self.gs=gs
        self.Soln=None
        self.ini=None
    def f(self,nodo):
        resp=self.gs[nodo]
        return resp
    def getHijos(self,nodo):
        resp=self.grafo[nodo]
        return resp
    def setIni(self,ini):
        self.ini=ini
    def getSoln(self):
        return self.Soln
    @abstractmethod
    def buscar(self):
        pass


class simAneal(local):
    def __init__(self,grafo,gs,kMax=10):
        super().__init__(grafo,gs)
        self.kMax=kMax
    def getHijoRnd(self,actual):
        hijos=self.getHijos(actual)
        nHijos=len(hijos)
        ind=np.random.randint(0,nHijos)
        resp=hijos[ind]
        return resp
    def Temperatura(self,valor):
        return pow(0.95,valor)
    def buscar(self):
        actual=self.ini
        for k in range(self.kMax):
            T=self.Temperatura(k)
            nuevo=self.getHijoRnd(actual)
            fnuevo=self.f(nuevo)
            factual=self.f(actual)
            if fnuevo<factual:
                actual=nuevo
            else:
                r=np.random.uniform(0,1)
                p=np.exp(-(fnuevo-factual)/T)
                if p>=r:
                    actual=nuevo
        self.Soln=actual