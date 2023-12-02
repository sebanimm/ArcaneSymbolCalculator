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

        # needMeso_100M -> 더 필요한 억단위 메소
        # maxLvMeso -> 만렙까지 드는 돈
        # defaultMeso -> 기본적으로 드는 메소

    def needMeso_100M_1stSym(self):
        defaultMeso = 3110000 
        needMeso_100M = 0
        maxLvMeso = 811490000 
        for lv in range(1, self.level):
            defaultMeso += 3960000
            needMeso_100M += defaultMeso
        needMeso_100M = maxLvMeso - needMeso_100M
        needMeso_100M = math.trunc(needMeso_100M / 100000000)
        return needMeso_100M

    def needMeso_100M_2ndSym(self):
        defaultMeso = 6220000
        needMeso_100M = 0
        maxLvMeso = 995980000
        for lv in range(1, self.level):
            defaultMeso += 4620000
            needMeso_100M += defaultMeso
        needMeso_100M = maxLvMeso - needMeso_100M
        needMeso_100M = math.trunc(needMeso_100M / 100000000)
        return needMeso_100M

    def needMeso_100M_3rdSym(self):
        defaultMeso = 9330000
        needMeso_100M = 0
        maxLvMeso = 1180470000
        for lv in range(1, self.level):
            defaultMeso += 5280000
            needMeso_100M += defaultMeso
        needMeso_100M = maxLvMeso - needMeso_100M
        needMeso_100M = math.trunc(needMeso_100M / 100000000)
        return needMeso_100M

    def needMeso_100M_otherSym(self):
        defaultMeso = 11196000
        needMeso_100M = 0
        maxLvMeso = 1341324000
        for lv in range(1, self.level):
            defaultMeso += 5940000
            needMeso_100M += defaultMeso
        needMeso_100M = maxLvMeso - needMeso_100M
        needMeso_100M = math.trunc(needMeso_100M / 100000000)
        return needMeso_100M

        # needMeso_10K -> 더 필요한 만단위 메소
        # maxLvMeso -> 만렙까지 드는 돈
        # defaultMeso -> 기본적으로 드는 메소
        
    def needMeso_10K_1stSym(self):
        defaultMeso = 3110000 #
        needMeso_100M = 0
        needMeso_10K = 0
        maxLvMeso = 811490000 
        for lv in range(1, self.level):
            defaultMeso += 3960000
            needMeso_100M += defaultMeso
        needMeso_100M = maxLvMeso - needMeso_100M
        needMeso_10K += math.trunc(needMeso_100M / 10000)
        needMeso_10K %= 10000
        return needMeso_10K

    def needMeso_10K_2ndSym(self):
        defaultMeso = 6220000
        needMeso_100M = 0
        needMeso_10K = 0
        maxLvMeso = 995980000
        for lv in range(1, self.level):
            defaultMeso += 4620000
            needMeso_100M += defaultMeso
        needMeso_100M = maxLvMeso - needMeso_100M
        needMeso_10K += math.trunc(needMeso_100M / 10000)
        needMeso_10K %= 10000
        return needMeso_10K
        

    def needMeso_10K_3rdSym(self):
        defaultMeso = 9330000
        needMeso_100M = 0
        needMeso_10K = 0
        maxLvMeso = 1180470000
        for lv in range(1, self.level):
            defaultMeso += 5280000
            needMeso_100M += defaultMeso
        needMeso_100M = maxLvMeso - needMeso_100M
        needMeso_10K += math.trunc(needMeso_100M / 10000)
        needMeso_10K %= 10000
        return needMeso_10K

    def needMeso_10K_otherSym(self):
        defaultMeso = 11196000
        needMeso_100M = 0
        needMeso_10K = 0
        maxLvMeso = 1341324000
        for lv in range(1, self.level):
            defaultMeso += 5940000
            needMeso_100M += defaultMeso
        needMeso_100M = maxLvMeso - needMeso_100M
        needMeso_10K += math.trunc(needMeso_100M / 10000)
        needMeso_10K %= 10000
        return needMeso_10K