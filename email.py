### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

class Email:

    has_been_read = False

    spam_email = False

    def __init__(self, email_address, subject_line, email_content):    
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.spam_email = True
        
    def __str__(self):
        return (f"\nSubject: {self.subject_line}\t\tFrom: {self.email_address}")

# --- Lists --- #
# Initialise an empty list to store the email objects.

Inbox_list = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():

    Inbox_list.append(Email("aaron@email.com", "I hate emails", "I have too many emails"))
    Inbox_list.append(Email("john@email.com", "I love emails", "I don't have enough emails"))
    Inbox_list.append(Email("greg@email.com", "I like emails", "I have just enough emails"))

    return Inbox_list

def spam_email():
    
    for index, email in enumerate(Inbox_list):
        print(f"{index + 1}. {email.email_address} - {email.subject_line}")

    while True:
        
        chosen_index = int(input("\nPlease input the index of the email you would like to read: "))
        if 1 <= chosen_index <= len(Inbox_list):
            chosen_email = Inbox_list[chosen_index - 1]
            is_spam = input("Is this a spam email?\nIf yes press 'y' if no press 'n': ")
            if is_spam == "y":
                chosen_email.mark_as_spam()
                print("This email has been moved to spam.")
                break
            elif is_spam == "n":
                break
            elif is_spam not in ["y", "n"]:
                print("Invaild response entered. Try again..")

def delete_email():

    for index, email in enumerate(Inbox_list):
        print(f"{index + 1}. {email.email_address} - {email.subject_line}")
        
    while True:
        
        chosen_index = int(input("\nPlease input the index of the email you would like to read: "))
        if 1 <= chosen_index <= len(Inbox_list):
            chosen_email = Inbox_list[chosen_index - 1]
            delete_email = input("Would you like to delete this email?\nIf yes press 'y' if no press 'n': ")
            if delete_email == "y":
                Inbox_list.remove(chosen_email)
                print("This email has been deleted.")
                break
            elif delete_email == "n":
                break
            elif delete_email not in ["y", "n"]:
                print("Invalid response entered. Try again..")
         
    # Create 3 sample emails and add it to the Inbox list.

def list_emails():

    for index, email in enumerate(Inbox_list):
        print(f"{index + 1}. {email.email_address} - {email.subject_line}")
        print("\n")
    
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.

def read_email():
             
    for index, email in enumerate(Inbox_list):
        print(f"{index + 1}. {email.email_address} - {email.subject_line}")

    chosen_index = int(input("\nPlease input the index of the email you would like to read: "))
    if 1 <= chosen_index <= len(Inbox_list):
        chosen_email = Inbox_list[chosen_index - 1]
        print("\n")
        print(f"From: {chosen_email.email_address} \n")
        print(f"Subject: {chosen_email.subject_line} \n")
        print(chosen_email.email_content)
        print("")
        print(f"\nEmail '{chosen_email.subject_line}' from {chosen_email.email_address} has now been marked as read.\n")
        chosen_email.mark_as_read() 
        return chosen_email
                               
    else:
        print("\nThe index entered does not correspond to an email index. Try again..")
    return read_email()

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. View spam emails
    4. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
         read_email()
        
    elif user_choice == 2:
        # add logic here to view unread emails
        if Email.has_been_read == False:
            for x in Inbox_list:
                print(f"\nSubject: {x.subject_line}\t\tFrom: {x.email_address}")
        else:
            print("\nAll emails have been read.\n")

    elif user_choice == 3:
        # add logic here to view spam emails
        for spam_emails in Inbox_list:
            print(f"From: {spam_emails.email_address}, Is spam: {spam_emails.spam_email}")
        else:
            print("\nYou have no assigned spam emails.\n")
   
    elif user_choice == 4:
        # add logic here to quit appplication
        quit()

    else:
        print("Oops - incorrect input.")