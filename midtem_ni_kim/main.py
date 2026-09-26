"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: Santos, Kim Aron C.
"""

pets = ["gagambino"]  # starts empty — the user adds pets as the program runs

def display_menu():
    # print the menu, return the user's choice
    print ("=== Pet Adoption Records ===")
    print (""" 
            1. Add a pet
            2. View all pets
            3. Count available vs adopted
            4. Find a pet by name
            5. Remove pets
            6. Exit
                                        """)


def add_pet(pet_list):
    # ask for name, animal type, status — build the string, add to the list
    put = input("What pet do u want to add? ")
    pets.append(put)

    print ("Successfully added.")

def view_pets(pet_list):
    # loop through and print every pet — handle empty list
    print (pets)

def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both
    print ("The total available pets:")
    print (len(pets))

def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_pet(pet_list):
    remove = input("What pet do u want to remove? ")
    # your code here

def main():
    running = True
    while running:
            # use if/elif to call the right function based on choice
            # set running = False when the user picks Exit
        display_menu()

        try:

            choice = int(input("What do you want to do? "))
            
            if choice == 1:
                add_pet(pets)
            elif choice == 2:
                view_pets(view_pets)
            elif choice == 3:
                count_available_adopted(count_available_adopted)
            elif choice == 4:
                find_pet
            elif choice == 5:
                remove_pet(remove_pet)
            elif choice == 6:
                running = False
            else: 
                print ("Just pick only on 1-5!!! ")

        except ValueError:
            print ("Enter a valid number... ")

main()