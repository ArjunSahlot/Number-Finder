num = int(input("Enter a number: "))

if num == 0 or num == 1 or num == 2:
    print("%d is a special number" % num)
    exit(0)

if num & 1 == 0:
    print("%d is not a prime number" % num)
    exit(0)

divisor = 3

while num % divisor != 0:
    divisor=divisor+2
    if divisor >= num/2:
        print("%d is not a prime number" % num)
        break

if divisor <= num/2:
    print("%d is a prime number" % num)