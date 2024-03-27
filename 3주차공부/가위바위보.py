import random

choices = ["가위", "바위", "보"]
computer = random.choice(choices)

user = input("가위, 바위, 보 중 하나를 선택하세요: ")

print("사용자 선택:", user)
print("컴퓨터 선택:", computer)

if (user == "가위" and computer == "보")or(user == "바위" and computer == "가위")or(user == "보" and computer == "바위") :
    print("사용자가 이겼습니다!")
elif user == computer :
    print("무승부입니다!")
else :
    print("컴퓨터가 이겼습니다!")