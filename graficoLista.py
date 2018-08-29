import matplotlib.pyplot as plt
from random import randint
import timeit

def generateList(size):
    listt = []
    for i in range(size):
        n = randint(1,1*size)
        if(n in listt):
          n = randint(1,1*size)
        listt.append(n)
    return listt

def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas"):
    plt.plot(x,y, label = "Melhor Tempo")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
 
sizeList = [100,1000,10000,20000,30000,40000,50000]
time=[]
 
for i in sizeList:
    tempo =   timeit.timeit("generateList({})".format(i),setup="from __main__ import generateList",number=1)
    time.append(tempo)
 
desenhaGrafico(time, sizeList, "Time", "Numbers")