from Arcane import Arcane
import math

print("""
1. 소멸의 여로
2. 츄츄 아일랜드
3. 레헬른
4. 아르카나
5. 모라스
6. 에스페라
""".strip())

symType = int(input("아케인 심볼의 종류: "))
symLv = int(input("아케인 심볼의 레벨: "))

userSym = int(input("아케인 심볼의 갯수: "))
userMeso_10K = int(input("메소 (억 단위): "))
userMeso_100M = int(input("메소 (만 단위): "))

maxSym = Arcane(20)
maxLv = maxSym.AccNeedLv()

userMeso_10K *= 10000
userMesoTotal = userMeso_10K + userMeso_100M

symbol = Arcane(symLv)

print(f"만렙까지 더 필요한 아케인 심볼은 {((maxLv) - Arcane(symLv).AccNeedLv()) - userSym}개 입니다")

# resultMeso_100M -> 억단위메소, resultMeso_10K -> 만단위 메소 
resultMeso_10K_1stSym = symbol.needMeso_10K_1stSym() - userMeso_100M # 필요한 만단위 메소 (1)
resultMeso_10K_2ndSym = symbol.needMeso_10K_2ndSym() - userMeso_100M # 필요한 만단위 메소 (2)
resultMeso_10K_3rdSym = symbol.needMeso_10K_3rdSym() - userMeso_100M # 필요한 만단위 메소 (3)
resultMeso_10K_otherSym = symbol.needMeso_10K_otherSym() - userMeso_100M # 필요한 만단위 메소 (4,5,6)
resultMeso_100M_1stSym = (symbol.needMeso_100M_1stSym()*10000) - userMeso_10K # 필요한 억단위 메소 (1)
resultMeso_100M_2ndSym = (symbol.needMeso_100M_2ndSym()*10000) - userMeso_10K # 필요한 억단위 메소 (2)
resultMeso_100M_3rdSym = (symbol.needMeso_100M_3rdSym()*10000) - userMeso_10K # 필요한 억단위 메소 (3)
resultMeso_100M_otherSym = (symbol.needMeso_100M_otherSym()*10000) - userMeso_10K # 필요한 억단위 메소 (4,5,6)

# symbolMeso->심볼 업그레이드 가격 (억단위 + 만단위) (1/2/3/4,5,6)
symbolMeso_1stSym = (symbol.needMeso_100M_1stSym()*10000) + symbol.needMeso_10K_1stSym()
symbolMeso_2ndSym = (symbol.needMeso_100M_2ndSym()*10000) + symbol.needMeso_10K_2ndSym()
symbolMeso_3rdSym = (symbol.needMeso_100M_3rdSym()*10000) + symbol.needMeso_10K_3rdSym()
symbolMeso_otherSym = (symbol.needMeso_100M_otherSym()*10000) + symbol.needMeso_10K_otherSym()
   
if symType == 1 :
    if resultMeso_10K_1stSym < 0 :
        resultMeso_10K_1stSym += 10000
        resultMeso_100M_1stSym -= 1
    if userMesoTotal < symbolMeso_1stSym :
        print(f"만렙까지 더 필요한 메소는 {math.trunc(resultMeso_100M_1stSym / 10000)}억 {resultMeso_10K_1stSym}만 메소입니다")
    else :
        print("만렙까지 필요한 메소는 충분합니다")
elif symType == 2 :
    if resultMeso_10K_2ndSym < 0 :
        resultMeso_10K_2ndSym += 10000
        resultMeso_100M_2ndSym -= 1
    if userMesoTotal < symbolMeso_2ndSym :
        print(f"만렙까지 더 필요한 메소는 {math.trunc(resultMeso_100M_2ndSym / 10000)}억 {resultMeso_10K_2ndSym}만 메소입니다")
    else :
        print("만렙까지 필요한 메소는 충분합니다")
elif symType == 3 :
    if resultMeso_10K_3rdSym < 0 :
        resultMeso_10K_3rdSym += 10000
        resultMeso_100M_3rdSym -= 1
    if userMesoTotal < symbolMeso_3rdSym :
        print(f"만렙까지 더 필요한 메소는 {math.trunc(resultMeso_100M_3rdSym / 10000)}억 {resultMeso_10K_3rdSym}만 메소입니다")
    else :
        print("만렙까지 필요한 메소는 충분합니다")
else:
    if resultMeso_10K_otherSym < 0 :
        resultMeso_10K_otherSym += 10000
        resultMeso_100M_otherSym -= 1
    if userMesoTotal < symbolMeso_otherSym :
        print(f"만렙까지 더 필요한 메소는 {math.trunc(resultMeso_100M_otherSym / 10000)}억 {resultMeso_10K_otherSym}만 메소입니다")
    else :
        print("만렙까지 필요한 메소는 충분합니다")