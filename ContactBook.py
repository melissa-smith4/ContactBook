#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os

#This function intakes the contact information and stores them in the contact dictionary.
def create_new_contact(contacts, name, phone, email):
    #Store the contact info in the dictionary where the name is the key and the list [phone, email] is the value. 
    contacts[name] = [phone, email]


#This function saves the contacts to the txt file.
def import_to_file(contacts):
    #Open the txt file in writign mode.
    with open("contacts_storage.txt", "w") as file:
        #Iterate through the contacts and write them into the file.
        for name, info in contacts.items():
            file.write(f"{name},{info[0]},{info[1]}\n")
    print("\nContacts saved to ContactBook.")
   

#This function loads the contacts from the txt file.
def open_from_file():
    contacts = {}
    #Check if a contacts txt file already exists. If so, load them into the contacts dictionary.
    if os.path.exists("contacts_storage.txt"):
        with open("contacts_storage.txt", "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts[name] = [phone, email]
   
    #Return the contacts. If no contacts exist, return empty dictionary.
    return contacts

#This function acts as a buffer after executing an action, allowing the user to choose whether
#to continue or to exit the program.
def buffer():
    option = (input("Enter Y to continue or N to exit program: ")).upper()
    #Ensure the user's option is either Y or N
    while (option != "Y") and (option != "N"):
       print("Invalid input. Please try again.\n")
       option = (input("Enter Y to continue or N to exit program: ")).upper()
    return option

#This is the main function that will conduct all the tasks.
def main():
    contacts = open_from_file()
    print("\nWelcome to ContactBook!")
    
    #This while loop iterates through the main tasks of the function.
    while True:
        #Ask the user what task they would like to do and intake their response.
        task = input(f"\nWhat would you like to do? \n 1. Create new contact \n 2. Edit contact \n 3. View all contacts \n 4. View specific contact \n 5. Delete contact \n 6. Close ContactBook \nEnter a task number: ")
        
        if task == "1":
            #Intake the new contact information from the user.
            #Capitalize the entire name to prevent issues with case sensitivity going forward.
            name_input = (input("\nEnter contact name: ")).upper()
            phone_input = input("Enter phone number: ")
            email_input = input("Enter email: ")
            
            #Use the create_new_contact function to save the contact information.
            create_new_contact(contacts, name_input, phone_input, email_input)
            print("\nContact saved.\n")
            
            #Prompt user to return to main menu or quit program
            user_option = buffer()
            if user_option == "N":
                import_to_file(contacts)
                return "\nThank you for using ContactBook! Have a nice day."
            else:
                continue
        
        
        elif task == "2":
            #Ask the user which contact they would like to edit and intake their response.
            name_input = (input("Enter the name of the contact you would like to edit: ")).upper()
            
            #If no contacts exist, let the user know and return to the main menu.
            if contacts == {}:
                print("\nNo contacts found! Please add contacts first and try again.\n")
            
            #If this contact is not found in contacts, prompt user to check the contact list and try again.
            elif name_input not in contacts:
                print("\nNo contact with this name exists. Please check the contact list and try again.\n")
            
            #Print the contact's curent information to the user and intake the updated phone number and email.
            else:
                print(f"\nThe current contact information for {name_input} is:\nName: {name_input}\n\tPhone: {contacts[name_input][0]}\n\tEmail: {contacts[name_input][1]}\n")
                phone_input = input("Please input the updated phone number: ")
                email_input = input("Please input the updated email: ")
                contacts[name_input] = [phone_input, email_input]
                print("\nContact updated.\n")
            
            #Prompt user to return to main menu or quit program
            user_option = buffer()
            if user_option == "N":
                import_to_file(contacts)
                return "\nThank you for using ContactBook! Have a nice day."
            else:
                continue
            
        
        elif task == "3":
            #If no contacts exist, let the user know and return to the main menu.
            if contacts == {}:
                print("\nNo contacts found! Please add contacts first and try again.\n")
            
            else:
                #Sort the contacts by turning the dictionary into a list, then sort, then revert to dictionary.
                contact_keys = list(contacts.keys())
                contact_keys.sort()
                sorted_contacts = {j: contacts[j] for j in contact_keys}
                
                print("\nSHOWING ALL CONTACTS:")
                #Iterate through the current contacts and print each one to the user.
                for name, info in sorted_contacts.items():
                    print(f"{name}\n\tPhone: {info[0]}\n\tEmail: {info[1]}\n")
            
            #Prompt user to return to main menu or quit program
            user_option = buffer()
            if user_option == "N":
                import_to_file(contacts)
                return "\nThank you for using ContactBook! Have a nice day."
            else:
                continue
        
        
        elif task == "4":
            #Ask the user which contact they would like to view and intake their response.
            name_input = (input("\nEnter the name of the contact you would like to view: ")).upper()
            
            #If no contacts exist, let the user know and return to the main menu.
            if contacts == {}:
                print("\nNo contacts found! Please add contacts first and try again.\n")
           
            #If this contact is not found in contacts, prompt user to check the contact list and try again.
            elif name_input not in contacts:
                print("\nNo contact with this name exists. Please check the contact list and try again.\n")
            
            #Print the information for the desired contact to the user.
            else: 
                print(f"\n{name_input}\n\tPhone: {contacts[name_input][0]}\n\tEmail: {contacts[name_input][1]}\n")
            
            #Prompt user to return to main menu or quit program
            user_option = buffer()
            if user_option == "N":
                import_to_file(contacts)
                return "\nThank you for using ContactBook! Have a nice day."
            else:
                continue
        
            
        elif task == "5":
            #Ask the user which contact they would like to delete and intake their response.
            name_del = (input("\nEnter the name of the contact you would like to delete: ")).upper()
            
            if name_del not in contacts:
                print("\nNo contact with this name exists. Please check the contact list and try again.\n")
          
            #Delete the contact from contacts.
            else:
                del contacts[name_del]
                print(f"\nThe contact information for {name_del} has been deleted.\n")
            
            #Prompt user to return to main menu or quit program
            user_option = buffer()
            if user_option == "N":
                import_to_file(contacts)
                return "\nThank you for using ContactBook! Have a nice day."
            else:
                continue
        
        
        elif task == "6":
            #Save the contacts to the txt file before closing the program.
            import_to_file(contacts)
            return "\nThank you for using ContactBook! Have a nice day."
        
        
        else:
            #If the user inputs text that is not a number from 1-6, prompt them to try again.
            print("\nInvalid input. Please try again.\n")
            continue


print(main())
