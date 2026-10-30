def missing_number_xor(numbers):
    n = len(numbers) + 1
    result = 0

    for i in range(1, n + 1):
        result ^= i

    for num in numbers:
        result ^= num

    return result


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Missing number:", missing_number_xor(numbers))



#c:\Raza\Second_Cl_Pipeline\Codes\count_words.py