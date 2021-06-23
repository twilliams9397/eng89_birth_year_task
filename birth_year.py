current_year = int(2021)

user_prompt = True
#
# while user_prompt:
#     age = input("What is your age in years (do not add months yet)?  ")
#     name = input("What is your name?  ").capitalize()
#     if age.isdigit():
#         birth_year = current_year - int(age)
#         print(f"OMG {name}, you are {age} years old so you were born in {birth_year}.")
#         user_prompt = False
#     else:
#         print("Please enter a valid age in digits.")

current_month = int(6)
current_day = int(23)

while user_prompt:
    name = input("What is your name?  ").capitalize()
    age = input("In digits, what is your age in years?  ")
    if age.isdigit():
        birth_month = input("In digits, what month were you born in? E.g. January would be month 1.  ")
        if birth_month.isdigit():
            age = int(age)
            birth_year = current_year - age
            birth_month = int(birth_month)
            if birth_month < current_month:
                print(f"You have had your birthday this year {name}, so you were born in {birth_year}")
                user_prompt = False
            elif birth_month > current_month:
                print(f"You have not had your birthday this year {name}, so you were born in {birth_year + 1}")
                user_prompt = False
            else:
                birth_day = input("In digits, what day were you born on?  ")
                if birth_day.isdigit():
                    birth_day = int(birth_day)
                    if birth_day < current_day:
                        print(f"You have had your birthday this year {name}, so you were born in {birth_year}")
                        user_prompt = False
                    elif birth_day > current_day:
                        print(f"You have not had your birthday this year {name}, so you were born in {birth_year + 1}")
                        user_prompt = False
                    else:
                        print(f"It is your birthday today, you were born in {birth_year}. Happy Birthday {name}!")
                        user_prompt = False
                else:
                    print("Please input your birth day as digits.")
        else:
            print("Please ensure the month is inputted as digits.")
    else:
        print("Please ensure the year is inputted as digits.")
    hours = age * int(8760) # hours in a year
    answer = input("Would you like to know how many hours you have lived to the year? Y/N  ")
    if answer.upper() == "Y":
        print(f"You have lived for {hours} hours {name}!")
    else:
        print("Ok, have a good day!")


