import string 
alphapet = string.ascii_lowercase
alphapet_ = string.ascii_uppercase
word = input("Enter a word: ")
space = int(input("Enter a shift number: "))
def encrypt(wordy, spacy):
    secret_word = ""
    for i in wordy:
        if i in alphapet:    
            pos = alphapet.index(i)
            new_pos = (pos + spacy) % 26
            secret_word += alphapet[new_pos]
        elif i in alphapet_:
            pos = alphapet_.index(i)
            new_pos = (pos + spacy) % 26
            secret_word += alphapet_[new_pos]
        else:
            secret_word += i
    print("The secret word is: "+ secret_word)
encrypt(wordy = word, spacy = space)