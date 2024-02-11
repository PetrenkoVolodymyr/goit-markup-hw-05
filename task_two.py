import re

def generator_numbers(text: str):
    numbers = re.findall(r"\s\d+\.\d+\s",text)
    for number in numbers:
        try:
            if type(float(number))==float:
                yield float(number)
        except:
            continue


def sum_profit(text, func):
    return sum(list(func(text)))


text = "10.0Загальний дохід працівника складається 65.56, з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів. 33.00"

print(sum_profit(text, generator_numbers))