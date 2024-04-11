import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)
print("첫 번째 무자위 수는 "+str(num1)+"입니다.")
print("두 번째 무자위 수는 "+str(num2)+"입니다.")
print("세 번째 무자위 수는 "+str(num3)+"입니다.")

mid = 0
if num1>num2 and num1<num3 :
    mid = num1
elif num2>num1 and num2<num3 : 
    mid = num2
else :
    mid = num3
print("\n세 정수 중 중간값은 "+str(mid)+"입니다.")
