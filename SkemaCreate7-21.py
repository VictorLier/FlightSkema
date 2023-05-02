import numpy as np
from numpy import random
oldObjFunc = 40


while True:

    #Antal Hold
    HoldN = 21

    #Antal både
    BoatN = np.arange(0,HoldN)

    #print(BoatN)

    #Antal både i hver sejlads
    split1 = int(7)
    split2 = int(14)


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
        AlleModAlle[Sejlads[0],Sejlads[1]] = AlleModAlle[Sejlads[0],Sejlads[1]] + 1
        AlleModAlle[Sejlads[0],Sejlads[2]] = AlleModAlle[Sejlads[0],Sejlads[2]] + 1
        AlleModAlle[Sejlads[0],Sejlads[3]] = AlleModAlle[Sejlads[0],Sejlads[3]] + 1
        AlleModAlle[Sejlads[0],Sejlads[4]] = AlleModAlle[Sejlads[0],Sejlads[4]] + 1
        AlleModAlle[Sejlads[0],Sejlads[5]] = AlleModAlle[Sejlads[0],Sejlads[5]] + 1
        AlleModAlle[Sejlads[0],Sejlads[6]] = AlleModAlle[Sejlads[0],Sejlads[6]] + 1
        AlleModAlle[Sejlads[1],Sejlads[0]] = AlleModAlle[Sejlads[1],Sejlads[0]] + 1
        AlleModAlle[Sejlads[1],Sejlads[2]] = AlleModAlle[Sejlads[1],Sejlads[2]] + 1
        AlleModAlle[Sejlads[1],Sejlads[3]] = AlleModAlle[Sejlads[1],Sejlads[3]] + 1
        AlleModAlle[Sejlads[1],Sejlads[4]] = AlleModAlle[Sejlads[1],Sejlads[4]] + 1
        AlleModAlle[Sejlads[1],Sejlads[5]] = AlleModAlle[Sejlads[1],Sejlads[5]] + 1
        AlleModAlle[Sejlads[1],Sejlads[6]] = AlleModAlle[Sejlads[1],Sejlads[6]] + 1
        AlleModAlle[Sejlads[2],Sejlads[0]] = AlleModAlle[Sejlads[2],Sejlads[0]] + 1
        AlleModAlle[Sejlads[2],Sejlads[1]] = AlleModAlle[Sejlads[2],Sejlads[1]] + 1
        AlleModAlle[Sejlads[2],Sejlads[3]] = AlleModAlle[Sejlads[2],Sejlads[3]] + 1
        AlleModAlle[Sejlads[2],Sejlads[4]] = AlleModAlle[Sejlads[2],Sejlads[4]] + 1
        AlleModAlle[Sejlads[2],Sejlads[5]] = AlleModAlle[Sejlads[2],Sejlads[5]] + 1
        AlleModAlle[Sejlads[2],Sejlads[6]] = AlleModAlle[Sejlads[2],Sejlads[6]] + 1
        AlleModAlle[Sejlads[3],Sejlads[0]] = AlleModAlle[Sejlads[3],Sejlads[0]] + 1
        AlleModAlle[Sejlads[3],Sejlads[1]] = AlleModAlle[Sejlads[3],Sejlads[1]] + 1
        AlleModAlle[Sejlads[3],Sejlads[2]] = AlleModAlle[Sejlads[3],Sejlads[2]] + 1
        AlleModAlle[Sejlads[3],Sejlads[4]] = AlleModAlle[Sejlads[3],Sejlads[4]] + 1
        AlleModAlle[Sejlads[3],Sejlads[5]] = AlleModAlle[Sejlads[3],Sejlads[5]] + 1
        AlleModAlle[Sejlads[3],Sejlads[6]] = AlleModAlle[Sejlads[3],Sejlads[6]] + 1
        AlleModAlle[Sejlads[4],Sejlads[0]] = AlleModAlle[Sejlads[4],Sejlads[0]] + 1
        AlleModAlle[Sejlads[4],Sejlads[1]] = AlleModAlle[Sejlads[4],Sejlads[1]] + 1
        AlleModAlle[Sejlads[4],Sejlads[2]] = AlleModAlle[Sejlads[4],Sejlads[2]] + 1
        AlleModAlle[Sejlads[4],Sejlads[3]] = AlleModAlle[Sejlads[4],Sejlads[3]] + 1
        AlleModAlle[Sejlads[4],Sejlads[5]] = AlleModAlle[Sejlads[4],Sejlads[5]] + 1
        AlleModAlle[Sejlads[4],Sejlads[6]] = AlleModAlle[Sejlads[4],Sejlads[6]] + 1
        AlleModAlle[Sejlads[5],Sejlads[0]] = AlleModAlle[Sejlads[5],Sejlads[0]] + 1
        AlleModAlle[Sejlads[5],Sejlads[1]] = AlleModAlle[Sejlads[5],Sejlads[1]] + 1
        AlleModAlle[Sejlads[5],Sejlads[2]] = AlleModAlle[Sejlads[5],Sejlads[2]] + 1
        AlleModAlle[Sejlads[5],Sejlads[3]] = AlleModAlle[Sejlads[5],Sejlads[3]] + 1
        AlleModAlle[Sejlads[5],Sejlads[4]] = AlleModAlle[Sejlads[5],Sejlads[4]] + 1
        AlleModAlle[Sejlads[5],Sejlads[6]] = AlleModAlle[Sejlads[5],Sejlads[6]] + 1
        AlleModAlle[Sejlads[6],Sejlads[0]] = AlleModAlle[Sejlads[6],Sejlads[0]] + 1
        AlleModAlle[Sejlads[6],Sejlads[1]] = AlleModAlle[Sejlads[6],Sejlads[1]] + 1
        AlleModAlle[Sejlads[6],Sejlads[2]] = AlleModAlle[Sejlads[6],Sejlads[2]] + 1
        AlleModAlle[Sejlads[6],Sejlads[3]] = AlleModAlle[Sejlads[6],Sejlads[3]] + 1
        AlleModAlle[Sejlads[6],Sejlads[4]] = AlleModAlle[Sejlads[6],Sejlads[4]] + 1
        AlleModAlle[Sejlads[6],Sejlads[5]] = AlleModAlle[Sejlads[6],Sejlads[5]] + 1

    #print(AlleModAlle)

    #Samlet i en lang:

    Samlet = AlleModAlle[0,1:HoldN]
    #print(AlleModAlle[1,0])
    for i in range(19):
        Samlet = np.append(Samlet, AlleModAlle[i+1,0:i+1],axis=0)
        Samlet = np.append(Samlet, AlleModAlle[i+1,i+2:HoldN],axis=0)
    Samlet = np.append(Samlet,AlleModAlle[20,0:20],axis=0)

    #print(Samlet)

    #Forskel på fleste og færreste indbyrdes kampe:
    DifMatch = np.max(Samlet) - np.min(Samlet)

    #print(DifMatch)


    #Matrix med hvor mange gange de sejler i hver båd
    Både = np.zeros((HoldN,7),dtype=int)

    for i in range(Skema.shape[0]):
        Sejlads = Skema[i]
        #print(Sejlads)
        Både[Sejlads[0],0] = Både[Sejlads[0],0] + 1
        Både[Sejlads[1],1] = Både[Sejlads[1],1] + 1
        Både[Sejlads[2],2] = Både[Sejlads[2],2] + 1
        Både[Sejlads[3],3] = Både[Sejlads[3],3] + 1
        Både[Sejlads[4],4] = Både[Sejlads[4],4] + 1
        Både[Sejlads[5],5] = Både[Sejlads[5],5] + 1
        Både[Sejlads[6],6] = Både[Sejlads[6],6] + 1

    #print(Både)

    Difbåd = np.max(Både) - np.min(Både)



    #print(Difbåd)

    ObjFunc = DifMatch     

    if ObjFunc == 4:
        BedsteSkema = Skema
        oldObjfunc = ObjFunc
        print(DifMatch)
        print(ObjFunc)
        np.savetxt("Skema.csv", Skema, fmt="%d", delimiter=",")
        np.savetxt("AlleModAlle.csv", AlleModAlle, fmt="%d", delimiter=",")
        np.savetxt("Både.csv", Både, fmt="%d", delimiter=",")
    
    
