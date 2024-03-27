member = int(input("MT 인원수 :"))
w1 = int(input("1인당 생수 개수 :"))

water =  member*w1
waterPack = water//15
waterPackPrice = 10000*(water//15)
wp = water%15
wpp = (water%15)*900
result = waterPackPrice+wpp

print("필요한 생수 개수 : "+str(water)+"개")
print("생수 팩 구매량 :"+str(waterPack)+"개, "+str(waterPackPrice)+"원")
print("생수 낱개 구매량 :"+str(wp)+"개, "+str(wpp)+"원")
print("생수 총 구매 비용 :"+str(result)+"원")
