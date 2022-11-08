import random


# Optimum happiness is 3000

def exploitOnly():
    happiness = 0
    cafeterias = []
    cafeteria1 = random.normalvariate(10, 8)
    cafeterias.append(cafeteria1)

    happiness += cafeteria1

    cafeteria2 = random.normalvariate(15, 6)
    cafeterias.append(cafeteria2)

    happiness += cafeteria2

    cafeteria3 = random.normalvariate(12, 5)
    cafeterias.append(cafeteria3)

    happiness += cafeteria3

    best = max(cafeterias)

    if best == cafeteria1:
        for x in range(297):
            happiness += random.normalvariate(10, 8)

    elif best == cafeteria2:
        for x in range(297):
            happiness += random.normalvariate(15, 6)

    else:
        for x in range(297):
            happiness += random.normalvariate(12, 5)

    print(happiness)

def exploreOnly():
    happiness = 0
    for x in range(100):
        happiness += random.normalvariate(10, 8)
        happiness += random.normalvariate(15, 6)
        happiness += random.normalvariate(12, 5)

    # return happiness
    print(happiness)

def eGreedy(e = 10):
    cafeterias = []
    happiness = 0

    cafeteria1 = random.normalvariate(10, 8)
    cafeteria2 = random.normalvariate(15, 6)
    cafeteria3 = random.normalvariate(12, 5)


    cafeterias.append(cafeteria1)
    cafeterias.append(cafeteria2)
    cafeterias.append(cafeteria3)

    best = max(cafeterias)


    r = random.random()
    if r < (e/100):
        i = random.randint(1,3)
        if i == 1:
            happiness += random.normalvariate(10, 8)
        elif i == 2:
            happiness += random.normalvariate(15, 6)
        else:
            happiness += random.normalvariate(12, 5)


    else:
        happiness += best


    return happiness



