def show_me_prime():
    print('prime\tfunkcion\tnumber_to\treturn list with prime number')


def prime(number_to):
    if number_to < 2:
        return []

    prime_numbers = []
    is_prime = [True] * (number_to + 1)
    is_prime[0] = is_prime[1] = False

    for number in range(2, number_to + 1):
        if is_prime[number]:
            prime_numbers.append(number)
            for multiple in range(number * number, number_to + 1, number):
                is_prime[multiple] = False
   

    return prime_numbers


