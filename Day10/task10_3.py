def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
    #print("This got printed")
    #print("This got printed")는 실행이 안된다 왜냐하면 return이 컴퓨터에게 이것이 함수의 끝임을 알려주고 이제 함수를 종료해야 한다고 말하기 때문

print(format_name(input("What is your first name?"), input("What is your last name?")))
s