from RegexValidations import *


def main():
    word1 = "31 998555287"
    word2 = "31998555287"
    word3 = "(31)998555287"

    regexValidations = RegexValidations()

    print(f'Phone1 match ? {regexValidations.matchPhone(word1)}')
    print(f'Phone2 match ? {regexValidations.matchPhone(word2)}')
    print(f'Phone3 match ? {regexValidations.matchPhone(word3)}')

    email = 'danilo.silva09@precato.com.br'

    print(f'Email match ? {regexValidations.matchEmail(email)}')


if __name__ == "__main__":
    main()
