# Name generator from 2 lists

import random

first_names_list = ["Jair", "Abraham", "Yzler", "Edgar"]

last_names_list = ["Parra", "Cheng", "Ortiz", "Baron"]

def name_generate():
    first_name = random.choice(first_names_list)
    last_name = random.choice(last_names_list)
    print(first_name, last_name)
    
    

def user_condition():
    choice = input("Generate name? y/n: ")
    choice = choice.lower()
    while choice == "y":
        name_generate()
        choice = input("Generate name? y/n: ")
        choice = choice.lower()
    else:
        print("Have a good day!")
            


user_condition()