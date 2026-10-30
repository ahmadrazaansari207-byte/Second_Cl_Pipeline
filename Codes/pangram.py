def pangram(sentence):
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in sentence.lower():
            return False

    return True


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(pangram(text))



#c:\Raza\Second_Cl_Pipeline\Code\pangram.py