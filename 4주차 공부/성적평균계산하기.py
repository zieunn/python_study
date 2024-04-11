# ?? 뭐가 문제징 ..ㅠ
n = 0
sum = 0
x = 0

print("종료하려면 음수를 입력하시오")

while (x >= 0) :
    x = int(input("성적을 입력하시오: "))
    sum = sum + x
    n+=1
result = sum / n
print("성적의 평균은 %f입니다." %result)