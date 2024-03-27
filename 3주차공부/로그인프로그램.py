#아이디를 입력받아서 등록된 아이디인지를 검사하는 프로그램
#list이용
userList = ["김지은", "김하은", "김은총"]

id = input("아이디: ")

if id in userList :
    password = input("패스워드를 입력하시오: ")
    if password == "20040330" :
        print("환영합니다.")
    else :
        print("잘못된 패스워드입니다.")
else : 
    print("알 수 없는 사용자입니다!")