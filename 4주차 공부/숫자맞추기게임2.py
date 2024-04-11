satement = input("문자열을 입력하시오: ")
word = 0
number = 0
spaces = 0

for w in satement :
    if w.isalpha() :  #w가 알파벳인지 판별
        word = word + 1
    if w.isdigit() :  #w가 숫자인지 판별
        number = number + 1
    if w.isspace() :  #w가 공백인지 판별
        spaces = spaces + 1

print("알파벳 문자의 개수=", word)
print("숫자 문자의 개수=", number)
print("스페이스 문자의 개수=", spaces)