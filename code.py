# first we need to import the shuffle
from random import shuffle
my_list = ['o','','']

def shuffle_num(my_list):
    shuffle(my_list)
    return my_list

#we need to take the input from use

def user_gess():
    guess = ''
    
    while guess not in ['0','1','2']:
        guess = input("Enter the number 0 or 1 or 2:")
        
        return int(guess)
        
# now to check the user guess 
def check_guess(guess,my_list):
    if my_list[guess] == 'o':
        print("Correct")
        print(my_list)
    else:
        print("ohh!! Wrong Guess Better Luck Next time")
        print(my_list)
        
        
mixed_list=shuffle_num(my_list)
guess_num = user_gess()

check_guess(guess_num,mixed_list)
