# Define the following variables
# name, last_name, age, eye_color, hair_color
name = ''
last_name = ''
eye_color = ''
hair_color = ''
# Prompt user for input and Re-assign these
f_name = input('What is your first name? \n')
l_name = input('What is your last name? \n')
age = int(input('What is your age this year? \n'))
eye_color = input('What is your eye color? \n')
hair_color = input('What is your hair color? \n')
# Extra - Cast your input
str_age = str(age)
# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
print(
    'Hello ' + f_name + '! Welcome, your age is ' + str_age + ', your eyes color is' + eye_color + 'and your hair color '
                                                                                               'is ' + hair_color)
# Section 2 - Calculate in what year was the person born? and respond back.

date_of_birth = 2020 - age
print('You said you we\'er this year' + str_age + ' hence you were born in ' + str(date_of_birth) + '!')
# print something like: 'You said you we're 28 hence you were born in 1991!'


