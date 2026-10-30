def first_non_repeating(text):
    for char in text:
        if text.count(char) == 1:
            return char

    return ""


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("First non-repeating character:", first_non_repeating(text))



#c:\Raza\Second_Cl_Pipeline\Codes\count_words.py