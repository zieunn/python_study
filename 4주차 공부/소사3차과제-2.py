number = input("학번을 입력하세요(단, 각 자리수는 띄어쓰기로 구분) : ")
x = number.split()

x = [int(num) for num in x]
result = []

sum = 0
for i in x :
    sum += i
    result.append(sum)

print("누적 합 리스트 :", result)
