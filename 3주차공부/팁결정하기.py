price = float(input("음식 값 입력: "))
print("팁을 선택하세요:")
print("1. 10%")
print("2. 15%")
print("3. 20%")

tip = int(input("팁 선택 (1/2/3): "))

if tip == 1 :
    choiceTip = 0.10
elif tip == 2 :
    choiceTip = 0.15
elif tip == 3 : 
    choiceTip = 0.20
else :
    print("올바른 선택이 아닙니다. 기본값인 15%로 계산합니다.")
    choiceTip = 0.15

print("음식 값: $"+str(price))
print("선택한 팁: "+str(choiceTip*100)+"%")
print("팁 금액: $"+str(price*choiceTip))
print("총 지불 금액: $"+str(price+(price*choiceTip)))



