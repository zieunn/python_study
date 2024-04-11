number = input()
sum = 0
for i in number :
    sum = sum + int(i)

print("자리수의 합은 %d입니다." %sum)


#다른 방법 이용 
num = int(input())
sum2 = 0

while num > 0 :
    num1 = num % 10
    sum2 = sum2 + num1
    num = num // 10

print("자리수의 합은 %d입니다." %sum2)