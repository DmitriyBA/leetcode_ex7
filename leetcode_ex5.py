import random

number = random.randint(1000, 10000)


def find_zero(array_zero: list) -> None:
    """
    Функция ищет ноль в списке элементов и удаляет его
    """
    for item in range(len(array_zero)):
        if array_zero[item] == 0:
            array_zero.pop(item)
            break


def discharge_number(num: int) -> list:
    """
    :param num: принимает число (int)
    :return: возвращает список из разрядов числа
    """
    array_digit = []
    while num:
        digit = num % 10
        array_digit.append(digit)
        num = num // 10
    array_digit.reverse()
    array_discharge = []
    for item in range(len(array_digit)-1, 0, -1):
        array_discharge.append(10**item)
    array_discharge.append(1)
    array_digit_result = []
    for item in range(len(array_discharge)):
        array_digit_result.append(array_digit[item]*array_discharge[item])
    count_zero = 0
    for item in range(len(array_digit_result)):
        if array_digit_result[item] == 0:
            count_zero += 1
    while count_zero != 0:
        find_zero(array_digit_result)
        count_zero -= 1
    return array_digit_result


array_digit_res = discharge_number(number)
print(array_digit_res)
