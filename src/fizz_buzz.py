def fizz_buzz(number):
    if number % 15 == 0:
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    elif number == 5:
        return 'buzz'
    else:
        return str(number)