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

SymType = int(input("아케인 심볼의 종류: "))
SymLv = int(input("아케인 심볼의 레벨: "))

UserSym = int(input("아케인 심볼의 갯수: "))
UserMeso_10K = int(input("메소 (억 단위): "))
UserMeso_100M = int(input("메소 (만 단위): "))

maxSym = Arcane(20)
maxLv = maxSym.AccNeedLv()

UserMeso_10K *= 10000
UserMesoTotal = UserMeso_10K + UserMeso_100M

Symbol = Arcane(SymLv)

print(f"만렙까지 더 필요한 아케인 심볼은 {((maxLv) - Arcane(SymLv).AccNeedLv()) - UserSym} 개 입니다")

# symbolMeso->심볼 업그레이드 가격 (억단위 + 만단위) (1/2/3/4,5,6)
symbolMeso_1stSym = (Symbol.NeedMeso_100M_1stSym()*10000) + Symbol.NeedMeso_10K_1stSym()
symbolMeso_2ndSym = (Symbol.NeedMeso_100M_2ndSym()*10000) + Symbol.NeedMeso_10K_2ndSym()
symbolMeso_3rdSym = (Symbol.NeedMeso_100M_3rdSym()*10000) + Symbol.NeedMeso_10K_3rdSym()
symbolMeso_otherSym = (Symbol.NeedMeso_100M_otherSym()*10000) + Symbol.NeedMeso_10K_otherSym()

# resultMeso_100M -> 억단위메소, resultMeso_10K -> 만단위 메소 
resultMeso_100M_1stSym = (Symbol.NeedMeso_100M_1stSym()*10000) - UserMeso_10K # 필요한 억단위 메소 (1)
resultMeso_100M_2ndSym = (Symbol.NeedMeso_100M_2ndSym()*10000) - UserMeso_10K # 필요한 억단위 메소 (2)
resultMeso_100M_3rdSym = (Symbol.NeedMeso_100M_3rdSym()*10000) - UserMeso_10K # 필요한 억단위 메소 (3)
resultMeso_100M_otherSym = (Symbol.NeedMeso_100M_otherSym()*10000) - UserMeso_10K # 필요한 억단위 메소 (4,5,6)
resultMeso_10K_1stSym = Symbol.NeedMeso_10K_1stSym() - UserMeso_100M # 필요한 만단위 메소 (1)
resultMeso_10K_2ndSym = Symbol.NeedMeso_10K_2ndSym() - UserMeso_100M # 필요한 만단위 메소 (2)
resultMeso_10K_3rdSym = Symbol.NeedMeso_10K_3rdSym() - UserMeso_100M # 필요한 만단위 메소 (3)
resultMeso_10K_otherSym = Symbol.NeedMeso_10K_otherSym() - UserMeso_100M # 필요한 만단위 메소 (4,5,6)
   
if SymType == 1 :
    if resultMeso_10K_1stSym < 0 :
        resultMeso_10K_1stSym += 10000
        resultMeso_100M_1stSym -= 1
    if UserMesoTotal < symbolMeso_1stSym :
        print(f"만렙까지 더 필요한 메소는 {math.trunc(resultMeso_100M_1stSym / 10000)}억 {resultMeso_10K_1stSym}만 메소입니다")
    else :
        print("만렙까지 필요한 메소는 충분합니다")
elif SymType == 2 :
    if resultMeso_10K_2ndSym < 0 :
        resultMeso_10K_2ndSym += 10000
        resultMeso_100M_2ndSym -= 1
    if UserMesoTotal < symbolMeso_2ndSym :
        print(f"만렙까지 더 필요한 메소는 {math.trunc(resultMeso_100M_2ndSym / 10000)}억 {resultMeso_10K_2ndSym}만 메소입니다")
    else :
        print("만렙까지 필요한 메소는 충분합니다")
elif SymType == 3 :
    if resultMeso_10K_3rdSym < 0 :
        resultMeso_10K_3rdSym += 10000
        resultMeso_100M_3rdSym -= 1
    if UserMesoTotal < symbolMeso_3rdSym :
        print(f"만렙까지 더 필요한 메소는 {math.trunc(resultMeso_100M_3rdSym / 10000)}억 {resultMeso_10K_3rdSym}만 메소입니다")
    else :
        print("만렙까지 필요한 메소는 충분합니다")
else:
    if resultMeso_10K_otherSym < 0 :
        resultMeso_10K_otherSym += 10000
        resultMeso_100M_otherSym -= 1
    if UserMesoTotal < symbolMeso_otherSym :
        print(f"만렙까지 더 필요한 메소는 {math.trunc(resultMeso_100M_otherSym / 10000)}억 {resultMeso_10K_otherSym}만 메소입니다")
    else :
        print("만렙까지 필요한 메소는 충분합니다")