def prime_checker(num):
    if num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                return print("It's not a prime number.")

        else:
            return print("It's a prime number.")


n = int(input("Check this number: "))

prime_checker(n)