# QUESTION 1

# Write a program that accepts user input to create a list of integers. Then, 
# compute the sum of all the integers in the list.

def main():
    input_str = input("Enter integers separated by spaces: ")
    numbers = [int(num) for num in input_str.split()]
    total = sum(numbers)
    print("List:", numbers)
    print("Sum:", total)

if __name__ == "__main__":
    main()


# QUESTION 2
# Create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.

tuple1 = ('book1', 'book2', 'book3', 'book4', 'book5')
for book in tuple1:
    print("\n")
    print(book)


# QUESTION 3
# Write a program that uses a dictionary to store information about a person, 
# such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.

user_details = {}
user_details['name']  = input("enter your firstname")
user_details['age'] = input("enter your age")
user_details['color'] = input("enter your favorite color")

print(user_details)
for key, value in user_details.items():
    print(f"{key.title()} {value}")

# QUESTION 4

# Write a program that accepts user input to create two sets of integers. Then, 
# create a new set that contains only the elements that are common to both sets.
def create_integer_set(set_name):
    print(f"\n enter integers for {set_name} (separated by spaces)")
    while True:
        try:
            user_input = input("> ")
            numbers = {int(num) for num in user_input.split()}
            return numbers
        except ValueError:
            print("invalid input, please enter integers separated by spaces")
set_a = create_integer_set("set A")
set_b = create_integer_set("Set B")
print("set A", set_a)
print("set B", set_b)
print("elements that are common in both sets are: ", set_a & set_b)