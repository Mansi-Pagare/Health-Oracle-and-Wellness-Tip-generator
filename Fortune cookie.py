# #importing relevant module
import random

# random integer
print(random.randint(1,10))
# random float
print(random.random())

# Ask the user for their choice
choice = input("Do you want to ask the Magic 8-Ball or open a Fortune Cookie? (Enter '8-ball' or 'fortune'): ").lower()

# magic ball logic
if choice == '8-ball':
    magic_ball = random.randint(1, 3)
    if magic_ball == 1:
        print ("yes")
    if magic_ball == 3:
        print ("no")
    if magic_ball == 2:
        print ("maybe")



#fortune cookie
elif choice == 'fortune':
#Creating variable
    lucky_number = random.randint(1,100)

    fortune_number = random.randint(1,3)

    fortune_text = ''

    if fortune_number ==1:
        fortune_text= "You will have a great day!... "
    elif fortune_number ==2:
        fortune_text= "Today will be tough but hang in there...!"
    elif fortune_number ==3:
        fortune_text= "You will get married at!"

    # Print ASCII art for the fortune cookie
    print("      _____")
    print("     /     \\")
    print("    /       \\")
    print("   /_________\\")
    print(f"  |  {fortune_text}")  
    print(f"  |  Lucky Number: {lucky_number} ")
    print("   \\_________/")

# Print the lucky number
    # print(f"{fortune_text}! Lucky number: {lucky_number}")

# Handling invalid input
else:
    print("Invalid choice. Please enter '8-ball' or 'fortune'.")