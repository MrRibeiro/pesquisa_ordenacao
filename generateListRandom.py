from random import randint
def generateList(size):
    listt = []
    for i in range(size):
        n = randint(1,1*size)
        if(n in listt):
          n = randint(1,1*size)
        listt.append(n)
    return listt
       
size = 1000
print(generateList(size))