def leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def check_date(date):
    day, month, year = map(int, date.split('.'))
    res = leap_year(year)

    if res is True:
        if month == 2:
            if 1 <= day <= 29:
                return True
            else:
                return False
        elif month in [4, 6, 9, 11]:
            if 1 <= day <= 30:
                return True
            else:
                return False
        else:
            if 1 <= day <= 31:
                return True
            else:
                return False
    else:
        if month == 2:
            if 1 <= day <= 28:
                return True
            else:
                return False
        elif month in [4, 6, 9, 11]:
            if 1 <= day <= 30:
                return True
            else:
                return False
        else:
            if 1 <= day <= 31:
                return True
            else:
                return False


if __name__ == '__main__':
    print(check_date('12.12.2000'))
    print(check_date('29.2.2023'))
