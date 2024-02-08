def generator_numbers(text: str):
    for word in text.split(' '):
        try:
            if type(float(word))==float:
                yield float(word)
        except:
            continue


def sum_profit(text):
    print(sum(list(generator_numbers(text))))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

sum_profit(text)