import sys


if len(sys.argv) == 2:
    num = int(sys.argv[1])
    if num <= 1:
        print('Not Valid!')

    else:
        is_prime = True
        for x in range(2, num):
            if num % x == 0:
                is_prime = False
                break

        if is_prime:
            print('The number is Prime')

        else:
            print('Its not prime')


else:
    print('Please enter a prime')


# Logic --> Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number
# using for loop

# def sieveOfErat(num):
#     # prime is an array of type boolean with True values in it
#     prime = [True for i in range(n + 1)]
#     p = 2
#     while (p * p <= n):
#       # If it remain unchanged it is prime
#         if (prime[p] == True):
#             # updating all the multiples
#             for i in range(p * 2, n + 1, p):
#                 prime[i] = False
#         p += 1
#     prime[0] = False
#     prime[1] = False
#     # Print
#     for p in range(n + 1):
#         if prime[p]:
#             print(p, end=" ")


# if __name__ == '__main__':
#     n = int(sys.argv[1])
#     print("The prime numbers smaller than or equal to", n, "is")
#     sieveOfErat(n)
