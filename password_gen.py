import random
import string
def my_password_gen():
    characters=list(string.ascii_letters)
    digits=list(string.digits)
    punctuation=list(string.punctuation)
    passlength=int(input("Enter password length:"))
    digitslength=int(input("Enter number of digits:"))
    letterslength=int(input("Enter number of letters:"))
    punctuationlength=int(input("Enter number of punctuations:"))
    length=digitslength + letterslength + punctuationlength
    random.shuffle(characters)
    random.shuffle(digits)
    random.shuffle(punctuation)
    new=[]
    if length<=passlength:
        for i in range(digitslength):
            new.append(random.choice(digits))
        for j in range(letterslength):
            new.append(random.choice(characters))
        for k in range(punctuationlength):
            new.append(random.choice(punctuation))
    elif length>passlength:
        return 0        
    random.shuffle(new)
    print("".join(new))

my_password_gen()
