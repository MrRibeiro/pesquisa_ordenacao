import matplotlib.pyplot as plt
from random import randint
import timeit
import numpy as np
import scipy.interpolate as interpolate
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

#countingSort
def sort(vetor, top):
    n = len(vetor)
    m = top + 1
    aux = [0] * m               
    for a in vetor:
        aux[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(aux[a]): 
            vetor[i] = a
            i += 1
    return vetor

def drawGraph(x,y,l,k,n, xl = "Nº de Elementos", yl = "Tempo(s)"):
    xnew = np.linspace(min(x), max(x), 10 * (max(x) - min(x)))
    a, b, c = interpolate.splrep(x, y, s=0, k=2)
    suave = interpolate.BSpline(a, b, c, extrapolate=False)
    plt.subplot(n)
    plt.plot(xnew, suave(xnew), label="Curva Suave: "+k)
    #plt.plot(x,y, label="Curva Sem Suaveização: "+k)
    plt.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.title(l, fontsize=12)

#template to sort list generated
def midCase(nums0):
    nums = nums0
    time = []
    for r in nums:
        print(r)
        vector = generateList(r)
        tempo = timeit.timeit("sort({},{})".format(vector, r),setup="from __main__ import sort",number=1)
        time.append(tempo)

    drawGraph(nums, time,'Counting Sort', "Caso Medio",111, "Nº de Elementos", "Tempo(s)")

def worseCase(nums1):
    nums=nums1
    time1=[]
    for r in nums:
        print (r)
        vector1 = listDesc(r)
        tempo = timeit.timeit("sort({},{})".format(vector1, r),setup="from __main__ import sort",number=1)
        time1.append(tempo)

    drawGraph(nums, time1, 'Counting Sort', "Pior Caso",111, "Nº de Elementos", "Tempo(s)")

# def bestCase(nums2):
#     nums=nums2
#     time2=[]
#     for r in nums:
#         print (r)
#         vector1 = listAsc(r)
#         tempo = timeit.timeit("sort({},{})".format(vector1, r),setup="from __main__ import sort",number=1)
#         time2.append(tempo)

#     drawGraph(nums, time2, 'Counting Sort', "Melhor Caso",111, "Nº de Elementos", "Tempo(s)")

midCase(numbers)
worseCase(numbers)
#bestCase(numbers)
plt.show()