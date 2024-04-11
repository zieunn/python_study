word_list = []
word = ""

while word != "quit" :
    word = input("단어를 입력하세요 ('quit'으로 종료): ")
    if word != "quit" : 
        word_list.append(word)

count = len(word_list)
print("입력된 단어 개수:", count)
print("입력된 단어 목록:", word_list)