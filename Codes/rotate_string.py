def rotate_string(text, k):
    if not text:
        return ""

    k = k % len(text)

    return text[-k:] + text[:-k] if k != 0 else text


if __name__ == "__main__":
    text = input("Enter a string: ")
    k = int(input("Enter rotation positions: "))

    print("Rotated string:", rotate_string(text, k))



#c:\Raza\Second_Cl_Pipeline\Codes\rotate_string.py