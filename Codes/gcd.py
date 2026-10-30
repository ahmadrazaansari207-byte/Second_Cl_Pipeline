def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return abs(a)


if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("GCD =", gcd(a, b))



#c:\Raza\Second_Cl_Pipeline\Codes\count_words.py