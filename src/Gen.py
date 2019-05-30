import numpy as np
import operator
import collections
from abc import ABC,abstractmethod

class ambiente(ABC):
	def __init__(self,grafo,fs):
		super().__init__()
		self.grafo=grafo
		self.fs=fs
	def getGrafo(self):
		return self.grafo
	def getFs(self):
		return self.fs
	def getHijos(self,actual):
		return self.grafo[actual]
	def getF(self,actual):
		return self.fs[actual]

class local(ABC):
	def __init__(self,proble):
		super().__init__()
		self.proble=proble
		self.ini=None
		self.Soln=None
	def setIni(self,edo):
		self.ini=edo
	@abstractmethod
	def siguiente(self,actual):
		pass
	@abstractmethod
	def buscar(self):
		pass


class alGen(local):
	def __init__(self,proble,genes):
		super().__init__(proble)
		self.genes=genes
	def letra2gen(self,letra):
		return self.genes[letra]
	def gen2letra(self,gen):
		return list(self.genes.keys())[list(self.genes.values()).index(gen)]
	def cruzar(self,padre,madre):
		n=len(padre)
		pCruza=np.random.randint(0,n)
		hijo=padre[0:pCruza]+madre[pCruza:n]
		return hijo
	def mutar(self,individuo):
		n=len(individuo)
		pMuta=np.random.randint(0,n-1)
		bit=individuo[pMuta]
		if bit=='0':
			respu=individuo[:pMuta]+'1'+individuo[pMuta+1:]
		else:
			respu=individuo[:pMuta]+'0'+individuo[pMuta+1:]
		return respu
	def seleccionar(self,poblacion):
		n=len(poblacion)
		suma=0
		for p in poblacion:
			fp=self.proble.getF(p)
			suma=suma+fp
		prs={}
		for p in poblacion:
			fp=self.proble.getF(p)
			prs[p]=fp/suma
		prs_lista=sorted(prs.items(),key=operator.itemgetter(1))
		prs=collections.OrderedDict(prs_lista)
		rangos={}
		anterior=0
		for p in poblacion:
			delta=prs[p]
			rangos[p]=[anterior,anterior+delta]
			anterior=anterior+delta
		padre=None
		madre=None
		r=np.random.uniform()
		for p in rangos:
			if r>=rangos[p][0] and r<=rangos[p][1]:
				padre=p
		r=np.random.uniform()
		for p in rangos:
			if r>=rangos[p][0] and r<=rangos[p][1]:
				madre=p
		return padre,madre
	def siguiente(self,poblacion):
		padre,madre=self.seleccionar(poblacion)
		genPadre=self.letra2gen(padre)
		genMadre=self.letra2gen(madre)
		hijo=self.cruzar(genPadre,genMadre)
		hijo=self.mutar(hijo)
		letraHijo=self.gen2letra(hijo)
		return letraHijo
	def buscar(self):
		p=self.genes.keys()
		total=len(p)
		maxItera=100
		nP=[]
		listo=False
		itera=1
		while not listo:
			for i in range(total):
				hijo=self.siguiente(p)
				nP.append(hijo)
			fmejor=0
			for p in nP:
				fp=self.proble.getF(p)
				if fp>fmejor:
					fmejor=fp
					mejor=p
			if itera<maxItera:
				itera=itera+1
			else:
				listo=True
		return mejor
