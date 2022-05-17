
PALINDROMES = [
    'Acaso hubo buhos aca',
    'A la catalana banal atacala',
    'Amar da drama',
]

NOT_PALINDROMES = [
    'Hola como estas',
    'Platzi'
    'Oscar',
]


def is_palindrome(palindrome):

    original = remove_minuscu(palindrome)
    procesed = voltear(original)

    if original == procesed:
        return True

    return False

    pass


def remove_minuscu(palabra):

    v = palabra.lower().replace(" ", "")
    return (v)


def voltear(g):

    a = "".join(reversed(g.lower()))
    return (a)


def validate():
    for palindrome in PALINDROMES:
        if not is_palindrome(palindrome):
            return False

    for not_palindrome in NOT_PALINDROMES:
        if is_palindrome(not_palindrome):
            return False
    return True


def run():
    if validate():
        print('Completaste el test')
    else:
        print('No completaste el test')


if __name__ == '__main__':
    run()
