import math
class Arcane:
    
    def __init__(self, level):
        self.level = level

    def NeedLv(self):
        return (self.level**2) + 11

    def AccNeedLv(self):
        AccLv = 0
        for lv in range(1, self.level):
            AccLv += (lv**2) + 11
        return AccLv

        # NeedMeso_100M -> 더 필요한 억단위 메소
        # MaxLvMeso -> 만렙까지 드는 돈
        # DefaultMeso -> 기본적으로 드는 메소

    def NeedMeso_100M_1stSym(self):
        DefaultMeso = 3110000 
        NeedMeso_100M = 0
        MaxLvMeso = 811490000 
        for lv in range(1, self.level):
            DefaultMeso += 3960000
            NeedMeso_100M += DefaultMeso
        NeedMeso_100M = MaxLvMeso - NeedMeso_100M
        NeedMeso_100M = math.trunc(NeedMeso_100M / 100000000)
        return NeedMeso_100M

    def NeedMeso_100M_2ndSym(self):
        DefaultMeso = 6220000
        NeedMeso_100M = 0
        MaxLvMeso = 995980000
        for lv in range(1, self.level):
            DefaultMeso += 4620000
            NeedMeso_100M += DefaultMeso
        NeedMeso_100M = MaxLvMeso - NeedMeso_100M
        NeedMeso_100M = math.trunc(NeedMeso_100M / 100000000)
        return NeedMeso_100M

    def NeedMeso_100M_3rdSym(self):
        DefaultMeso = 9330000
        NeedMeso_100M = 0
        MaxLvMeso = 1180470000
        for lv in range(1, self.level):
            DefaultMeso += 5280000
            NeedMeso_100M += DefaultMeso
        NeedMeso_100M = MaxLvMeso - NeedMeso_100M
        NeedMeso_100M = math.trunc(NeedMeso_100M / 100000000)
        return NeedMeso_100M

    def NeedMeso_100M_otherSym(self):
        DefaultMeso = 11196000
        NeedMeso_100M = 0
        MaxLvMeso = 1341324000
        for lv in range(1, self.level):
            DefaultMeso += 5940000 
        NeedMeso_100M = MaxLvMeso - NeedMeso_100M
        NeedMeso_100M = math.trunc(NeedMeso_100M / 100000000)
        return NeedMeso_100M

        # NeedMeso_10K -> 더 필요한 만단위 메소
        # MaxLvMeso -> 만렙까지 드는 돈
        # DefaultMeso -> 기본적으로 드는 메소
        
    def NeedMeso_10K_1stSym(self):
        DefaultMeso = 3110000 #
        NeedMeso_100M = 0
        NeedMeso_10K = 0
        MaxLvMeso = 811490000 
        for lv in range(1, self.level):
            DefaultMeso += 3960000
            NeedMeso_100M += DefaultMeso
        NeedMeso_100M = MaxLvMeso - NeedMeso_100M
        NeedMeso_10K += math.trunc(NeedMeso_100M / 10000)
        NeedMeso_10K %= 10000
        return NeedMeso_10K

    def NeedMeso_10K_2ndSym(self):
        DefaultMeso = 6220000
        NeedMeso_100M = 0
        NeedMeso_10K = 0
        MaxLvMeso = 995980000
        for lv in range(1, self.level):
            DefaultMeso += 4620000
            NeedMeso_100M += DefaultMeso
        NeedMeso_100M = MaxLvMeso - NeedMeso_100M
        NeedMeso_10K += math.trunc(NeedMeso_100M / 10000)
        NeedMeso_10K %= 10000
        return NeedMeso_10K
        

    def NeedMeso_10K_3rdSym(self):
        DefaultMeso = 9330000
        NeedMeso_100M = 0
        NeedMeso_10K = 0
        MaxLvMeso = 1180470000
        for lv in range(1, self.level):
            DefaultMeso += 5280000
            NeedMeso_100M += DefaultMeso
        NeedMeso_100M = MaxLvMeso - NeedMeso_100M
        NeedMeso_10K += math.trunc(NeedMeso_100M / 10000)
        NeedMeso_10K %= 10000
        return NeedMeso_10K

    def NeedMeso_10K_otherSym(self):
        DefaultMeso = 11196000
        NeedMeso_100M = 0
        NeedMeso_10K = 0
        MaxLvMeso = 1341324000
        for lv in range(1, self.level):
            DefaultMeso += 5940000 
        NeedMeso_100M = MaxLvMeso - NeedMeso_100M
        NeedMeso_10K += math.trunc(NeedMeso_100M / 10000)
        NeedMeso_10K %= 10000
        return NeedMeso_10K