def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input(""))

print(is_leap_year(year))

# udemy 해설
# 전체 주석 처리는 ctrl + /
# def is_leap_year(year):
#    if year % 4 == 0:
#        if year % 100 == 0:
#            if year % 400 == 0:
#                return True
#            else:
#                return False
#        else:
#            return True
#    else:
#        return False
