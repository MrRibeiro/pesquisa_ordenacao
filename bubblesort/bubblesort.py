# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from random import randint
import timeit
import numpy as np
import scipy.interpolate as interpolate
from threading import Thread
import sys 

reload(sys)  
sys.setdefaultencoding('utf8')

numbers = [1000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

#template to generate lists to be sorted
def generateList(size):
    listt = []
    for i in range(size):
        n = randint(1,100)
        if(n in listt):
          n = randint(1,100)
        listt.append(n)
    return listt

def listDesc(size):
    listt =[]
    while (size > 0):
        listt.append(size)
        size = size-1
    return listt

def listAsc(size):
    listt = []
    for i in range(size):
        listt.append(i+1)
    return listt

#bubblesort
def sort(vector):
    size = len(vector)
    while(size > 1):
        troca = False
        x = 0
        while(x < (size-1)):
            if(vector[x] > vector[x+1]):
                troca = True
                aux= vector[x]
                vector[x] = vector[x+1]
                vector[x+1] = aux
            x +=1
        if not troca:
            break
        size -= 1

    return vector

def drawGraph(x,y,l, n, xl = "Nº de Elementos", yl = "Tempo(s)"):
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.subplot(n)
    plt.plot(xnew, suave(xnew), label="Curva Suave")
    plt.plot(x,y, label="Curva Não Suave")
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title(l, fontsize=12)

#template to sort list generated
def midCase(nums1):
	numbers = nums1
	time = []
	for r in numbers:
	    print(r)
	    vector = generateList(r)
	    tempo = timeit.timeit("sort({})".format(vector),setup="from __main__ import sort",number=1)
	    time.append(tempo)

	drawGraph(numbers, time,'Caso Medio',211, "Nº de Elementos", "Tempo(s)")

def worseCase(nums1):
	numbers=nums1
	time1=[]
	for r in numbers:
		print (r)
		vector1 = listDesc(r)
		tempo = timeit.timeit("sort({})".format(vector1),setup="from __main__ import sort",number=1)
		time1.append(tempo)

	drawGraph(numbers, time1, 'Pior Caso',212, "Nº de Elementos", "Tempo(s)")
    
midCase(numbers)
worseCase(numbers)
plt.show()