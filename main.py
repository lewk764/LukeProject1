#SDF Project 1: Custom Cars by Luke Rau

#Display a fancy intro/title
print("==================")
print("Welcome to the UMBC")
print("Car Customization Form!")
print("==================")
print()

#Multiple Choice instructions
print("For multiple choice problems, please enter the letter of the selection you want to order")

#Question 1
  #Provide user with selection for q 1
print("~ Make & Model ~")
print("1. What model of car would you like?")
print("     a. Thunder McKing")
print("     b. Drof D150")
print("     c. RAM DDR3")
print("     d. Hodna  Civil")
  #Create q1 variable and prompt user to supply their selection, and make a new line
ques1 = input("Please enter your selection ('a' - 'd'): ")
print()

#Question 2
  #Provide user with selection for q 2
print("2. Would you like to upgrade from the 4-door option to the 2-door option?")
  #Create q2 variable and prompt user to supply their selection, and make a new line
ques2 = input("Please enter your selection ('yes' or 'no'): ")
print()

#Question 3
  #Provide user with selection for q 3
print("~ Exterior ~")
print("3. What color would you like your car to be?")
  #Create q3 variable and prompt user to supply their selection, and make a new line
ques3 = input("Please type the color you would like: ")
print()

#Question 4
  #Provide user with selection for q 4
print("4. What style of headlights would yout like?")
print("     a. Normal")
print("     b. Can't see anything MK2")
print("     c. No one else can see anything MK5")
print("     d. Forbidden RGB Headlights 9000")
  #Create q4 variable and prompt user to supply their selection, and make a new line
ques4 = input("Please enter your selection ('a' - 'd'): ")
print()

#Question 5
  #Provide user with selection for q 5
print("~ Interior ~")
print("5. What interior style would you like?")
print("     a. '3rd Degree Burns in the summer' black leather ")
print("     b. Babushka's favorite rug style")
print("     c. 'For the love of god don't spill anything' white leather")
print("     d. Red Shag carpet style")
  #Create q5 variable and prompt user to supply their selection, and make a new line
ques5 = input("Please enter your selection ('a' - 'd'): ")
print()

#Question 6
  #Provide user with selection for q 6
print("6. Would you like heated seats?")
  #Create q6 variable and prompt user to supply their selection, and make a new line
ques6 = input("Please enter your selection ('yes' or 'no'): ")
print()

#Order summary output
print("==================")
print("~ Order Summary~")
print("==================")
print(f"Model Selection: {ques1}")
print(f"Upgrade to 2-door: {ques2}")
print(f"Desired Color: {ques3}")
print(f"Headlight Selection: {ques4}")
print(f"Interior Style Selection {ques5}")
print(f"Include Heated Seats: {ques6}")
