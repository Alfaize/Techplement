contacts = [
    {"name": "John", "contact": "8991617456"},
    {"name": "Mike", "contact": "7790017456"},
    {"name": "Albert","contact": "8097388401"},
    {"name": "Sara", "contact": "1234567890"}
]

def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("List of contacts:")
        for c in contacts:
            print(f"Name: {c['name']}, Contact: {c['contact']}")


def add_contact():
  print("Enter the contact you want to add i.e name and contact:")
  name = input("Enter name: ")
  contact = input("Enter contact: ")
  if not contact.isdigit() or len(contact) != 10:
        print("Invalid contact number. Please enter a valid contact number.")
        return
  for c in contacts:
        if c["contact"] == contact:
            print("Contact already exists")
            return
  contacts.append({"name": name, "contact": contact})
  print("Added successfully")


def search_contact(contacts):
  print("Enter the contact you want to search i.e name or contact:")
  search = input("Enter name or contact: ")
  found = False
  for c in contacts:
     if c["name"] == search or c["contact"] == search:
        print(f"Name found: {c['name']}, Contact found: {c['contact']}")
        found = True
        break   
  if not found:
   print("Contact not found")
     

def update_contact():
  print("Enter the name of the contact you want to update:")
  search_name = input("Enter name: ")
  found = False
  for c in contacts:
    if c["name"]==search_name:
       print("Enter the new contact details:")
       new_name=input("Enter new name")
       new_contact=input("Enter new contact:")

       if new_name:
          c["name"]=new_name
       if new_contact:
          c["contact"]=new_contact

       print("contact updated successfully")
       found = True
       break
  if not found:
    print("Contact not found")

def display_menu():
    print("\n Menu:")
    print("1. Add a Contact")
    print("2. Search for a Contact")
    print("3. Update a Contact")
    print("4. Display Contacts")
    print("5. Exit the Program")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-4).")
main()



