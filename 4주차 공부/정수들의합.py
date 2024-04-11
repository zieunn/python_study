#반복을 이용한 정수합 프로그램
x = int(input("어디까지 계산할까요: "))
sum = 0

for x in range(1, x+1) :
    sum = sum + x
print("1부터",x,"까지의 정수의 합=",sum)
