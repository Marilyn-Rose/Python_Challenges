#Write a function in Python that accepts a credit card number.
#It should return a string where all the characters are hidden 
#with an asterisk except the last four. 
#For example, if the function gets sent “4444444444444444”, 
#then it should return “4444”.

cc_num = input("Enter Credit Card Number: ")


def CCnum_to_hidden(cc_num):
    if len(cc_num) != 16:
        return "Invalide Credit Card Number"
    
    last_four_digits = cc_num[-4:]
    hidden_num = '*' * 12
    return hidden_num + last_four_digits

print (CCnum_to_hidden(cc_num))