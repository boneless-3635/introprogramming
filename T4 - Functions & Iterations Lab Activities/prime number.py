def is_prime(num):
    prime = False
    for i in range(2, int(num / 2 + 1)):
        if num % i != 0:
            prime = True
            print("This is a prime number")
            break
    if not prime:
        print("This is not a prime number")


is_prime(int(input("Enter number: ")))
