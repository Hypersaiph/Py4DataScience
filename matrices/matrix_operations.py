# Import numpy
import numpy as np
import warnings
warnings.filterwarnings('ignore')
# operations over matrix
Sdict = {"2005": 0, "2006": 1, "2007": 2, "2008": 3, "2009": 4, "2010": 5, "2011": 6, "2012": 7, "2013": 8, "2014": 9}
# Salaries
KobeBryant_Salary = [15946875, 17718750, 19490625, 21262500, 23034375, 24806250, 25244493, 27849149, 30453805, 23500000]
JoeJohnson_Salary = [12000000, 12744189, 13488377, 14232567, 14976754, 16324500, 18038573, 19752645, 21466718, 23180790]
LeBronJames_Salary = [4621800, 5828090, 13041250, 14410581, 15779912, 14500000, 16022500, 17545000, 19067500, 20644400]
CarmeloAnthony_Salary = [3713640, 4694041, 13041250, 14410581, 15779912, 17149243, 18518574, 19450000, 22407474,
                         22458000]
DwightHoward_Salary = [4493160, 4806720, 6061274, 13758000, 15202590, 16647180, 18091770, 19536360, 20513178, 21436271]
ChrisBosh_Salary = [3348000, 4235220, 12455000, 14410581, 15779912, 14500000, 16022500, 17545000, 19067500, 20644400]
ChrisPaul_Salary = [3144240, 3380160, 3615960, 4574189, 13520500, 14940153, 16359805, 17779458, 18668431, 20068563]
KevinDurant_Salary = [0, 0, 4171200, 4484040, 4796880, 6053663, 15506632, 16669630, 17832627, 18995624]
DerrickRose_Salary = [0, 0, 0, 4822800, 5184480, 5546160, 6993708, 16402500, 17632688, 18862875]
DwayneWade_Salary = [3031920, 3841443, 13041250, 14410581, 15779912, 14200000, 15691000, 17182000, 18673000, 15000000]
Pdict = {"KobeBryant": 0, "JoeJohnson": 1, "LeBronJames": 2, "CarmeloAnthony": 3, "DwightHoward": 4, "ChrisBosh": 5,
         "ChrisPaul": 6, "KevinDurant": 7, "DerrickRose": 8, "DwayneWade": 9}
# Field Goals
KobeBryant_FG = [978, 813, 775, 800, 716, 740, 574, 738, 31, 266]
JoeJohnson_FG = [632, 536, 647, 620, 635, 514, 423, 445, 462, 446]
LeBronJames_FG = [875, 772, 794, 789, 768, 758, 621, 765, 767, 624]
CarmeloAnthony_FG = [756, 691, 728, 535, 688, 684, 441, 669, 743, 358]
DwightHoward_FG = [468, 526, 583, 560, 510, 619, 416, 470, 473, 251]
ChrisBosh_FG = [549, 543, 507, 615, 600, 524, 393, 485, 492, 343]
ChrisPaul_FG = [407, 381, 630, 631, 314, 430, 425, 412, 406, 568]
KevinDurant_FG = [306, 306, 587, 661, 794, 711, 643, 731, 849, 238]
DerrickRose_FG = [208, 208, 208, 574, 672, 711, 302, 0, 58, 338]
DwayneWade_FG = [699, 472, 439, 854, 719, 692, 416, 569, 415, 509]
# matrix
FieldGoals = np.array(
    [KobeBryant_FG, JoeJohnson_FG, LeBronJames_FG, CarmeloAnthony_FG, DwightHoward_FG, ChrisBosh_FG, ChrisPaul_FG,
     KevinDurant_FG, DerrickRose_FG, DwayneWade_FG])
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
# Matrix
Salary = np.array([KobeBryant_Salary, JoeJohnson_Salary, LeBronJames_Salary, CarmeloAnthony_Salary, DwightHoward_Salary,
                   ChrisBosh_Salary, ChrisPaul_Salary, KevinDurant_Salary, DerrickRose_Salary, DwayneWade_Salary])
# Minutes Played
KobeBryant_MP = [3277, 3140, 3192, 2960, 2835, 2779, 2232, 3013, 177, 1207]
JoeJohnson_MP = [3340, 2359, 3343, 3124, 2886, 2554, 2127, 2642, 2575, 2791]
LeBronJames_MP = [3361, 3190, 3027, 3054, 2966, 3063, 2326, 2877, 2902, 2493]
CarmeloAnthony_MP = [2941, 2486, 2806, 2277, 2634, 2751, 1876, 2482, 2982, 1428]
DwightHoward_MP = [3021, 3023, 3088, 2821, 2843, 2935, 2070, 2722, 2396, 1223]
ChrisBosh_MP = [2751, 2658, 2425, 2928, 2526, 2795, 2007, 2454, 2531, 1556]
ChrisPaul_MP = [2808, 2353, 3006, 3002, 1712, 2880, 2181, 2335, 2171, 2857]
KevinDurant_MP = [1255, 1255, 2768, 2885, 3239, 3038, 2546, 3119, 3122, 913]
DerrickRose_MP = [1168, 1168, 1168, 3000, 2871, 3026, 1375, 0, 311, 1530]
DwayneWade_MP = [2892, 1931, 1954, 3048, 2792, 2823, 1625, 2391, 1775, 1971]
# Matrix
MinutesPlayed = np.array(
    [KobeBryant_MP, JoeJohnson_MP, LeBronJames_MP, CarmeloAnthony_MP, DwightHoward_MP, ChrisBosh_MP, ChrisPaul_MP,
     KevinDurant_MP, DerrickRose_MP, DwayneWade_MP])

print(Salary[Pdict["LeBronJames"]][Sdict["2009"]])

FieldGoalsPerGame = np.matrix.round(FieldGoals / Games)
print(FieldGoalsPerGame[Pdict["KobeBryant"]][Sdict["2009"]])

print(MinutesPlayed)