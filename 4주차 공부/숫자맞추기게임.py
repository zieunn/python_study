import random
number = random.randint(1, 100)

print("1부터 100사이의 숫자를 맞추시오")

count = 0
while count < 10 :
    user = int(input("숫자를 입력하시오: "))
    count = count + 1
    if user < number :
        print("낮음!")
    elif user > number : 
        print("높음!")
    else :
        break

if user == number :
    print("축하합니다. 시도횟수=", count)
else :
    print("정답은", number)