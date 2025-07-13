first_name = input("enter your first name: ") # lets you input your first name
print("your first name is", first_name.capitalize()) # outputs a string and a variable first_name but capitalized

surname = input("enter your surname: ") # lets you input your surname
print("your surname is", surname.capitalize()) # outputs a string and a variable surname but capitalised

phone_number = input("enter your phone number: ") # lets you input a phone number
print('your number is', phone_number) # outputs a string and a variable phone_number

first_name = first_name.capitalize()
surname = surname.capitalize()
# ↑↑↑ Capitalizing variables first_name and surname as shown above

def hello(firstname, surname): # defines a function hello
    print("hello world".capitalize())  # capitalizes value "hello world"
    print(f"Hi, {firstname} {surname}") # outputs a string "Hi, " with variables first_name and surname injected in the string


hello(first_name, surname) # calls the function hello


