
# # Open a new ticket
def new_ticket(service_tickets):
      while True:
            customer = input("Enter customers name: ")
            issue = input("Enter the issue: ")
            count = len(service_tickets) + 1
            print(count)
            service_tickets[f"Ticket{str(count)}"]  = {"Customer": customer, "Issue": issue, "Status": "open"}
            print(service_tickets)
            break

    
# # Updating the status of the existing ticket.
    
def updated(service_tickets):   
    try:
        update_t = input("Which ticket do you need to update? ").title() 
        print(update_t)
        print(update_t in service_tickets)
        if update_t in service_tickets:
            service_tickets[update_t]["Status"] = "closed" 
            print(service_tickets)
        else:
            raise ValueError("Ticket is not in a system.")
    except:
        print("Invalid input.")

       
# Showing tickets with status "open".

def open(service_tickets):
    for ticket in service_tickets:
        if service_tickets[ticket]["Status"] == "open":
            print(service_tickets[ticket]) 
        else:
            print("Not found.")
     
# Showing tickets with status "closed".

def closed(service_tickets):
    print(service_tickets.items())
    for ticket in service_tickets:
        if service_tickets[ticket]["Status"] == "closed":
            print(service_tickets[ticket])
        else:
            print("Not found.")
                             
                  
def system():   
    # Dict to store tickets(key) and info(value)

    service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "open"}
}

    # Create a menu
    while True:
           choice = input ('''
        Would you like to:
        - - - - - - - - - 
        1.) open new ticket
        2.) update ticket status 
        3.) open status tickets
        4.) closed status tickets
        5.) quit
        >''').lower()
           
           if choice == "quit" or choice == "5":
                print("Have a nice day!")
                break
           elif choice == "open new ticket" or choice == "1":
                 new_ticket(service_tickets)
           elif choice == "update ticket status" or choice == "2":
                 updated(service_tickets)
           elif choice == "open status tickets" or choice == "3":
                 open(service_tickets)
           elif choice == "closed status tickets" or choice == "4":
                 closed(service_tickets)
           else:
                 print("Invalid response, please try again.")

system()