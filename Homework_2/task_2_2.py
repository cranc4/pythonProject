# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

def fraction_conversion(number):
    numerator, denominator = number.split('/')
    return int(numerator), int(denominator)


def reduction(nom, den):
    def all_devs(number):
        all_dev = set()
        for dev in range(1, number // 1 + 1):
            if not number % dev:
                all_dev.add(dev)
        return all_dev

    nom_dev = all_devs(nom)
    den_dev = all_devs(den)
    reduct = max(nom_dev.intersection(den_dev))

    return str(nom // reduct), str(den // reduct)


def summ(first_number, second_number):
    first, second = fraction_conversion(first_number), fraction_conversion(second_number)

    if first[1] == second[1]:
        nom = first[0] + second[0]
        den = first[1]
        return '/'.join(reduction(nom, den))
    else:
        nom = first[0] * second[1] + first[1] * second[0]
        den = first[1] * second[1]
        return '/'.join(reduction(nom, den))


def multi(first_number, second_number):
    first, second = fraction_conversion(first_number), fraction_conversion(second_number)
    nom = first[0] * second[0]
    den = first[1] * second[1]
    return '/'.join(reduction(nom, den))


first_number = input('Введите первую дробь в формате a/b: ')
second_number = input('Введите вторую дробь в формате a/b: ')

print(f'Сумма: {summ(first_number, second_number)}')
print(f'Произведение: {multi(first_number, second_number)}')