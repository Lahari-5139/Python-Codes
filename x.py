n = input("Enter a number:")
def isPrime(n):
    con = "true"
    if (n != 2):
        for i in range (2,n):
            if (n % i == 0):
                con = "false"
    return (con)
print isPrime(n)