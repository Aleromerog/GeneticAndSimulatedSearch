import src.Gen as Gen
import src.Simu as Simu

def main():
    graph={'A':['B','C','D'],
        'B':['A','C','F'],
        'C':['A','B','D','E'],
        'D':['A','C','L'],
        'E':['C','F'],
        'F':['B','E','G'],
        'G':['F','H','J','K'],
        'H':['C','G','I'],
        'I':['H','J','M'],
        'J':['G','I','N'],
        'K':['G','O'],
        'L':['C','D','M'],
        'M':['I','L','N'],
        'N':['J','M','O'],
        'O':['K','N'],
        'P':[]}
    weigths={'A':29,'B':12,'C':10,'D':20,'E':9,'F':6,'G':15,'H':20,'I':32,'J':30,'K':25,'L':8,'M':12,'N':12,'O':8, 'P':0.01}
    genes={'A':"0000",'B':"0001",'C':"0010",'D':"0011",'E':"0100",'F':"0101",
       'G':"0110",'H':"0111",'I':"1000",'J':"1001",'K':"1010",'L':"1011",
       'M':"1100",'N':"1101",'O':"1110", 'P':"1111"}


    problem2 = Simu.simAneal(graph, weigths, 12)
    problem2.setIni('A')
    problem2.buscar()
    print("Solución Con templado simulaodo para la menor utilidad: " + problem2.getSoln())
    problem = Gen.ambiente(graph, weigths)
    search = Gen.alGen(problem, genes)
    soultion = search.buscar()
    print("Solución con Algoritmo Genético con máxima utilidad: " + soultion)

if __name__=="__main__":
    main()

    