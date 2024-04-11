money = 1000
year = 0

while money < 2000 :
    year = year + 1
    interest = money * 0.05
    money = interest + money

print("기간:", year)
print("총액:", money)