import numpy as np
from itertools import permutations
from scipy.optimize import minimize
Div = 1

if Div == 1:
    HoldN = 21
    BådeN = 7
elif Div == 2:
    HoldN = 27
    BådeN = 9




def ObjFun(params):
    List = np.arange(0,HoldN)
    Flights = np.tile(List,(12,1))
    params = 
    print(params)
    for i in range(12):
        np.random.seed(params[i])
        np.random.shuffle(Flights[i])
    
    Skema = Flights.reshape((12*3),BådeN)

    #Matrix med hvor mange gange de møder hindanden
    AlleModAlle = np.zeros((HoldN,HoldN),dtype=int)

    #print(Skema.shape)

    for i in range(Skema.shape[0]):
        Sejlads = Skema[i]
        #print(Sejlads)
        for x in range(BådeN):
            for y in range(BådeN):
                AlleModAlle[Sejlads[x],Sejlads[y]] = AlleModAlle[Sejlads[x],Sejlads[y]] + 1

    #print(AlleModAlle)

    #Samlet i en lang:

    Samlet = AlleModAlle[0,1:HoldN]
    #print(AlleModAlle[1,0])
    for i in range(HoldN-2):
        Samlet = np.append(Samlet, AlleModAlle[i+1,0:i+1],axis=0)
        Samlet = np.append(Samlet, AlleModAlle[i+1,i+2:HoldN],axis=0)
    Samlet = np.append(Samlet,AlleModAlle[(HoldN-1),0:(HoldN-1)],axis=0)

    #Forskel på fleste og færreste indbyrdes kampe:
    DifMatch = np.max(Samlet) - np.min(Samlet)

    #print(DifMatch)


    #Matrix med hvor mange gange de sejler i hver båd
    Både = np.zeros((HoldN,BådeN),dtype=int)

    for i in range(Skema.shape[0]):
        Sejlads = Skema[i]
        #print(Sejlads)
        for x in range(BådeN):
            Både[Sejlads[x],x] = Både[Sejlads[x],x] + 1    

    #print(Både)

    Difbåd = np.max(Både) - np.min(Både)

    #print(Difbåd)

    BådeMinN = np.count_nonzero(Både == np.min(Både))
    BådeMaxN = np.count_nonzero(Både == np.max(Både))

    SamletMinN = np.count_nonzero(Samlet == np.min(Samlet))
    SamletMaxN = np.count_nonzero(Samlet == np.max(Samlet))


    ObjFunc = DifMatch*4 + Difbåd*2 + (BådeMaxN + BådeMinN + SamletMaxN + SamletMinN)*0.1


    return ObjFunc

print(ObjFun([1,2,3,4,5,6,7,8,9,2,3,4]))


initial_guess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(ObjFun(initial_guess))

res = minimize(ObjFun, initial_guess, method="CG")

print("Minimum value:", res.fun)