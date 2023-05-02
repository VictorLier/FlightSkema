import numpy as np
from numpy import random

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


AlleModAlle = np.zeros((HoldN,HoldN),dtype=int)

print(Skema.shape)


for i in range(Skema.shape[0]):
    Sejlads = Skema[i]
    print(Sejlads)
    AlleModAlle[Sejlads[0],Sejlads[1]] = AlleModAlle[Sejlads[0],Sejlads[1]] + 1
    AlleModAlle[Sejlads[0],Sejlads[2]] = AlleModAlle[Sejlads[0],Sejlads[2]] + 1
    AlleModAlle[Sejlads[0],Sejlads[3]] = AlleModAlle[Sejlads[0],Sejlads[3]] + 1
    AlleModAlle[Sejlads[0],Sejlads[4]] = AlleModAlle[Sejlads[0],Sejlads[4]] + 1
    AlleModAlle[Sejlads[0],Sejlads[5]] = AlleModAlle[Sejlads[0],Sejlads[5]] + 1
    AlleModAlle[Sejlads[0],Sejlads[6]] = AlleModAlle[Sejlads[0],Sejlads[6]] + 1

print(AlleModAlle)

for i in range(HoldN):
    for x in range(HoldN):
        AlleModAlle[i,x] = AlleModAlle[i,x] + AlleModAlle[x,i]

print(AlleModAlle)

