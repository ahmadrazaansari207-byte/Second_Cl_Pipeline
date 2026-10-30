def check_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False

    return True


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(check_sorted(numbers))



#c:\Raza\Second_Cl_Pipeline\Codes\check_sorted.py