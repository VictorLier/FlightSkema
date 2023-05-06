import numpy as np
from numpy import random
oldObjFunc = 100
Time = 0
oldTime = 0
Div = 1

if Div == 1:
    #Antal Hold
    HoldN = 21
    #Antal både i hver sejlads
    BådeN = 7

elif Div == 2:
    HoldN = 27
    BådeN = 9

#Antal både
BoatN = np.arange(0,HoldN)
#print(BoatN)
split1 = int(BådeN)
split2 = int(BådeN*2)

while True:
    #Sejladser
    np.random.shuffle(BoatN)
    r1 = BoatN[:split1]
    r2 = BoatN[split1:split2]
    r3 = BoatN[split2:]


    #print(r1)
    #print(r2)
    #print(r3)

    Flight = np.vstack((r1,r2,r3))

    #Første flight:
    Skema = Flight
    #print(Skema)

    #Næste 11 flights
    for i in range(11):
        np.random.shuffle(BoatN)
        r1 = BoatN[:split1]
        r2 = BoatN[split1:split2]
        r3 = BoatN[split2:]
        Flight = np.vstack((r1,r2,r3))
        Skema = np.vstack((Skema, Flight))

    #print(Skema)


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

    #print(Samlet)

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

    if ObjFunc < oldObjFunc:
        BedsteSkema = Skema
        oldObjFunc = ObjFunc
        #print(DifMatch)
        print(ObjFunc, Time, Difbåd, DifMatch)
        #print(oldObjFunc)
        Skema = Skema + 1
        if Div == 1:
            np.savetxt("Skema1.csv", Skema, fmt="%d", delimiter=",")
            np.savetxt("AlleModAlle1.csv", AlleModAlle, fmt="%d", delimiter=",")
            np.savetxt("Både1.csv", Både, fmt="%d", delimiter=",")
        else:
            np.savetxt("Skema2.csv", Skema, fmt="%d", delimiter=",")
            np.savetxt("AlleModAlle2.csv", AlleModAlle, fmt="%d", delimiter=",")
            np.savetxt("Både2.csv", Både, fmt="%d", delimiter=",")
    
    Time = Time + 1

    if Time > oldTime+10000:
        print(Time)
        oldTime = Time
    
    
    
