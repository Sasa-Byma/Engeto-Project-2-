import random

hidden_num = ''
guessed_num = ''


def hidden():
    """
    () --> str
    Generate a random 4 digit number.
    """
    global hidden_num
    hidden_num = str(random.randint(1000, 10000))
    while not validate_hidden(hidden_num):
        hidden_num = str(random.randint(1000, 10000))
    return hidden_num


def validate_hidden(hidden_num):
    """
    () --> Bool
    Check if digits do not repeat:
    """
    for i in hidden_num:
        if hidden_num.count(i) != 1:
            return False
    return True


def guess():
    """
    () --> str
    Pick a 4 digit number.
    """
    global guessed_num
    guessed_num = input('Enter your guess, please >>>>')
    while not validate_guess(guessed_num):
        guessed_num = input('Try again, please')
    return guessed_num


def validate_guess(guessed_num):
    """
    () --> Bool
   Return True if the number was entered correctly.
    """

    if len(guessed_num) != 4:
        print('Enter 4 digits!')
        return False
    if not guessed_num.isdigit():
        print('Enter numbers only!')
        return False
    if guessed_num[0] == '0':
        print('First digit can not be a zero!')
        return False
    for i in guessed_num:
        if guessed_num.count(i) != 1:
            print('Do not repeat digits!')
            return False
    return True


def bulls_and_cows(hidden_num, guessed_num):
    """
    (str, str) --> List
    Generate a random 4 digit number.
    """
    counter_bulls = 0
    counter_cows = 0
    for i in range(4):
        if hidden_num[i] == guessed_num[i]:
            counter_bulls += 1
    for i in range(4):
        for j in range(4):
            if hidden_num[i] == guessed_num[j]:
                counter_cows += 1
    return counter_bulls, counter_cows - counter_bulls


def welcome():
    print('''
    Welcome to the herd of Bulls and Cows

    You have 10 attempts to find hidden 4 digit number.

    Enter 4 digits.
    Number can not start with 0.
    Do not repeat digits.
    Enter digits only.
    ''')


def main():
    attempts = 0
    while (attempts < 10) and (hidden_num != guessed_num):
        print('Attempt number:', attempts + 1)
        guess()
        result = (bulls_and_cows(hidden_num, guessed_num))
        print('Bulls:', result[0], 'and Cows', result[1])
        print('')
        attempts += 1
    if attempts < 10:
        print('Good job!')
    else:
        print('Sorry, try another time! The hidden number was', hidden_num)


welcome()
hidden()
main()
