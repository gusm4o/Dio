from datetime import date, time, datetime


def use_date():
    data_atual = date.today()
    data_atual_srt = data_atual.strftime('%d-%m-%Y')
    print(data_atual.strftime('%d-%m-%Y'))


def use_time():
    horaro_str = time(hour=15, minute=18, second=55)
    horario = time(hour=15, minute=18, second=55)
    print(horario.strftime('%H:%M:%S'))
    print(type(horario))


def use_datetime():
    data_real = datetime.now()
    print(data_real)
    print(data_real.strftime('%H:%M'))
    print(data_real.year)
    data_str = '07/10/1994'
    data_conv = datetime.strptime(data_str, '%d/%m/%Y')
    print(data_conv)


if __name__ == '__main__':
    use_datetime()
    use_time()
    use_date()
