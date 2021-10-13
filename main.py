"""
Sectiune non-UI
"""


# 6


def get_longest_div_k(number_list, k):
    left = -1
    right = -1
    length = -1
    good_left = -1
    good_right = -1

    for number in number_list:
        right += 1

        if number % k == 0:
            if left == -1:
                left = right
        else:
            if left != -1 and (right - left) > length:
                length = right - left
                good_left = left
                good_right = right

            left = -1

    if left != -1 and (right - left - 1) > length:
        good_left = left
        good_right = right

    return number_list[good_left:good_right]


def test_get_longest_div_k():
    assert get_longest_div_k([2, 3, 4, 5, 6, 7], 2) == [2]
    assert get_longest_div_k([1, 3, 2, 13, 16, 6], 3) == [3]


# 13
def only_primes(number):
    primes = [2, 3, 5, 7]

    while number:
        digit = number % 10
        if digit not in primes:
            return False
        number //= 10

    return True


def get_longest_prime_digits(number_list):
    left = -1
    right = -1
    length = -1
    good_left = -1
    good_right = -1

    for number in number_list:
        right += 1

        if only_primes(number):
            if left == -1:
                left = right
        else:
            if left != -1 and (right - left) > length:
                length = right - left
                good_left = left
                good_right = right

            left = -1

    if left != -1 and (right - left - 1) > length:
        good_left = left
        good_right = right

    return number_list[good_left:good_right]


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([12, 14, 57, 53, 27, 93]) == [57, 53, 27]
    assert get_longest_prime_digits([45, 23, 72, 237, 63, 54]) == [23, 72, 237]


def is_palindrome(number):
    tmp = number
    inv = 0
    while tmp != 0:
        inv = inv * 10 + tmp % 10
        tmp = tmp // 10
    if inv == number:
        return True
    return False


def get_longest_all_palindromes(number_list):
    left = -1
    right = -1
    length = -1
    good_left = -1
    good_right = -1

    for number in number_list:
        right += 1

        if is_palindrome(number):
            if left == -1:
                left = right
        else:
            if left != -1 and (right - left) > length:
                length = right - left
                good_left = left
                good_right = right

            left = -1

    if left != -1 and (right - left - 1) > length:
        good_left = left
        good_right = right

    return number_list[good_left:good_right]


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([121, 12345, 65756, 4, 22, 150]) == [65756, 4, 22]
    assert get_longest_all_palindromes([7432, 43, 77, 45654, 1, 98]) == [77, 45654, 1]


"""
Sectiune UI
"""


def print_menu():
    print("1. Citire date")
    print("2. Determinare cea mai lungă subsecvență unde toate numerele sunt divizibile cu k (citit)")
    print("3. Determinare cea mai lungă subsecvență unde toate numerele sunt formate din cifre prime")
    print("4. Ieșire")


def read_list():
    numbers = []
    length = int(input('Lungimea listei: '))

    while length:
        numbers.append(int(input('Numar: ')))
        length -= 1

    return numbers


def solve_first_task(numbers):
    k = int(input('Introduceti k: '))
    answer = get_longest_div_k(numbers, k)
    print(answer)


def solve_second_task(numbers):
    answer = get_longest_prime_digits(numbers)
    print(answer)


def solve_third_task(numbers):
    answer = get_longest_all_palindromes(numbers)
    print(answer)


def start():
    numbers = []

    while True:
        print_menu()

        command = input("Comanda: ")

        if command == '1':
            numbers = read_list()
        elif command == '2':
            solve_first_task(numbers)
        elif command == '3':
            solve_second_task(numbers)
        elif command == '4':
            return
        else:
            print("Comanda invalida!")


def test():
    test_get_longest_div_k()
    test_get_longest_prime_digits()
    test_get_longest_all_palindromes()


start()
