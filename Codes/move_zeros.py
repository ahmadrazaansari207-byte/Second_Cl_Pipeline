def move_zeros(numbers):
    result = []
    zeros = 0

    for num in numbers:
        if num == 0:
            zeros += 1
        else:
            result.append(num)

    for i in range(zeros):
        result.append(0)

    return result


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Result:", move_zeros(numbers))



#c:\Raza\Second_Cl_Pipeline\Codes\move_zeros.py