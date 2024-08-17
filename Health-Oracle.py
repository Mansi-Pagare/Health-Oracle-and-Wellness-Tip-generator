# #importing relevant module
import random

# random integer
print(random.randint(1,10))
# random float
print(random.random())

# Ask the user for their choice
choice = input("Do you want to ask the Health Oracle or receive a Wellness Tip? (Enter 'oracle' or 'wellness'): ").lower()

# Health Oracle
if choice == 'oracle':
    oracle_response = random.randint(1, 3)
    if oracle_response == 1:
        print("Remember to stay hydrated today!")
    elif oracle_response == 2:
        print("Take a deep breath, your health is your wealth!")
    elif oracle_response == 3:
        print("A good night's sleep is the key to a healthy life!")



#Wellness Tip
elif choice == 'wellness':
#Creating variable
    lucky_number = random.randint(1,100)

    fortune_number = random.randint(1,3)

    fortune_text = ''

    if fortune_number ==1:
        fortune_text= "Take a walk outside, your body will thank you!... "
    elif fortune_number ==2:
        fortune_text= "Eat your greens for a balanced diet!"
    elif fortune_number ==3:
        fortune_text= "Don't forget to take time for self-care!"

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
    print("Invalid choice. Please enter 'oracle' or 'wellness'.")
