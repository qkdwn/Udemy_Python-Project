#{key: value} #딕셔너리

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
}

#print(programming_dictionary["Function"])

#프로그램의 뒷부분에서 딕셔너리에 새로운 값을 추가해야한다면 어떻게 해야할까?
programming_dictionary["Loop"] = "The action of doing something over and over again"

#빈 딕셔너리 만들기
empty_dictionary = {}

#기존 딕셔너리 확장
#programming_dictionary = {}
#print(programming_dictionary)

#딕셔너리 값 수정
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

#딕셔너리 반복문
for key in programming_dictionary:
    print(key) #key 값만 제공
    print(programming_dictionary[key]) #value 값만 제공