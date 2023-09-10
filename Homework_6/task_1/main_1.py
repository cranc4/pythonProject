# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv
from date_check import check_date

print(check_date(argv[1]))