def count_words(sentence):
    words = sentence.split()
    return len(words)


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Word count:", count_words(text))



#c:\Raza\Second_Cl_Pipeline\Codes\count_words.py