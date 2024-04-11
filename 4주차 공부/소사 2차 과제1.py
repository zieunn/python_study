hour = int(input("근무한 시간: "))
pay = 12800

if hour >= 4 :
    if hour >= 40 :
        food = (hour // 4) * 10000
        bonus = (pay * hour + food) * 0.1
    else :
        food = (hour // 4) * 9000
        bonus = (pay * hour + food) * 0.02
else :
    food = 0
    bonus = (pay * hour + food) * 0.02

result = pay * hour + food + bonus
result = round(result)
print("급여 : " + str(result) + "원")




        