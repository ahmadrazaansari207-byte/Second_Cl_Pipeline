def most_frequent(numbers):
    if not numbers:
        return None

    frequent = numbers[0]
    max_count = 0

    for num in numbers:
        count = numbers.count(num)

        if count > max_count:
            max_count = count
            frequent = num

    return frequent


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print("Most frequent element:", most_frequent(numbers))



#c:\Raza\Second_Cl_Pipeline\Codes\most_frequent.py