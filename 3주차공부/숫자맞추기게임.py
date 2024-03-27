from random import randint

computer = randint(1, 100)
print("숫자 게임에 오신 것을 환영합니다.")
number = int(input("숫자를 맞춰 보세요: "))

if number == computer :
    print("사용자가 이겼습니다.")
elif number > computer :
    print("너무 큼!")
else :
    print("너무 작음!")

print("게임종료")
