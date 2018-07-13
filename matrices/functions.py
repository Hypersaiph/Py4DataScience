# c l a s s i c
import numpy as np
import matplotlib.pyplot as plt
import random


def myplot(listofplayers):
    colors = ['Black', 'Red', 'Green', 'Blue', 'Magenta']
    markers = ['s', 'o', '^', 'D']
    for name in listofplayers:
        plt.plot(Games[Pdict[name]], c=random.choice(colors), ls='--', marker=random.choice(markers), ms=7, label=name)

    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.xticks(list(range(0, 10)), Seasons, rotation='vertical')
    plt.show()


Seasons = ["2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]
Players = ["KobeBryant", "JoeJohnson", "LeBronJames", "CarmeloAnthony", "DwightHoward", "ChrisBosh", "ChrisPaul",
           "KevinDurant", "DerrickRose", "DwayneWade"]
Pdict = {"KobeBryant": 0, "JoeJohnson": 1, "LeBronJames": 2, "CarmeloAnthony": 3, "DwightHoward": 4, "ChrisBosh": 5,
         "ChrisPaul": 6, "KevinDurant": 7, "DerrickRose": 8, "DwayneWade": 9}
# Games
KobeBryant_G = [80, 77, 82, 82, 73, 82, 58, 78, 6, 35]
JoeJohnson_G = [82, 57, 82, 79, 76, 72, 60, 72, 79, 80]
LeBronJames_G = [79, 78, 75, 81, 76, 79, 62, 76, 77, 69]
CarmeloAnthony_G = [80, 65, 77, 66, 69, 77, 55, 67, 77, 40]
DwightHoward_G = [82, 82, 82, 79, 82, 78, 54, 76, 71, 41]
ChrisBosh_G = [70, 69, 67, 77, 70, 77, 57, 74, 79, 44]
ChrisPaul_G = [78, 64, 80, 78, 45, 80, 60, 70, 62, 82]
KevinDurant_G = [35, 35, 80, 74, 82, 78, 66, 81, 81, 27]
DerrickRose_G = [40, 40, 40, 81, 78, 81, 39, 0, 10, 51]
DwayneWade_G = [75, 51, 51, 79, 77, 76, 49, 69, 54, 62]
# Matrix
Games = np.array([KobeBryant_G, JoeJohnson_G, LeBronJames_G, CarmeloAnthony_G, DwightHoward_G, ChrisBosh_G, ChrisPaul_G,
                  KevinDurant_G, DerrickRose_G, DwayneWade_G])

myplot(Players)