# generate pi to nth digit
# Chudnovsky algorihtm to find pi to n-th digit
# from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
import decimal


def compute_pi(n):
    decimal.getcontext().prec = n
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i+1) ** 3)
        #M = (K**3 - (K<<4)) * M / ((i+1)**3)
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
    pi = C / S
    return pi


while True:
    n = int(input("Please type number of decimals, between 0-1000, you'd like to display: "))
    if n >= 0 and n <= 1000:
        break
    else:
        print ("Please select a number between 0-1000")

print(compute_pi(n))
