# 2. Python Programming Challenges for Customer Service Data Handling
# Task 1: Customer Service Ticket Tracker Demonstrate your ability to 
# use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, 
# customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket.
# Display all tickets or filter by status.
# Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:

import json
import os

# This function will take in service_tickets and checks if the ticket_id is in the dictionary. If not, it will ask the user
# for input to fulfull all the value entries. I have set the default value of "Status" to be open at the initiation of a ticket.
def new_ticket(service_tickets, ticket_id):
    if ticket_id not in service_tickets:
        service_tickets.update({ticket_id:{"Customer": input("What is the customer name?\n"),
                                          "Issue": input("Give a brief description of the problem.\n"),
                                          "Status": "open"}})
        print(f"Ticket {ticket_id} has been created. The status is currently 'open'.")
    else:
        print(f"Ticket ID {ticket_id} is already in the system.")

# This function will take in service_tickets and iterate through the ticket_id
def update_ticket(service_tickets, ticket_id, status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id].update({"Status":status})
        print(f"Service ticket {ticket_id} has been updated with Status of '{status}'.")
    else:
        print("That ticket was not found. Please open a new ticket.")

# For conciseness I set a new variable 'sorted_dict' and set it to the dictionary conversion of the sorted tuples. lambda is set to the key
# and the item accesses the second set of dictionaries and utilizes the key 'Status' to sort by. I then set the reverse to be True to have the
# 'open' tickets first in the now sorted dictionary

def show_tickets(service_tickets):
    sorted_dict = dict(
    sorted(service_tickets.items(), key=lambda item: item[1]['Status'], reverse=True))
    print(json.dumps(sorted_dict, indent=4))
        



service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
    "Ticket003": {"Customer": "Jacob", "Issue": "Connection issue", "Status": "open"},
    "Ticket004": {"Customer": "Jennifer", "Issue": "Login problem", "Status": "closed"}
}

while True:
    print("\n")
    print("Please make a selection:\n1. Create a new ticket\n2. Update an existing ticket\n3. Show all tickets\n4. Exit Program")
    selection = input("Please type the number of your selection and hit 'Enter'.\n")

    match selection:
        case '1':
            os.system('cls||clear')
            new_ticket(service_tickets, input("Please enter the ID of the ticket.\n"))
        case '2':
            os.system('cls||clear')
            update_ticket(service_tickets, input("Please enter the ID of the ticket.\n"), input("What is the status of this ticket?\n"))
        case '3':
            os.system('cls||clear')
            show_tickets(service_tickets)
        case '4':
            os.system('cls||clear')
            print("Closing program.....")
            break
        case _:
            print("Input not recognized, please make a new selection.")