import random

names = ["Angela", "Ben", "Jenny", "Michael", "Cloe"]

random_choice = random.randint(0, 4)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + "is going to buy the meal today!")