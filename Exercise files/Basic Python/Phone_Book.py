import os
import csv


phones = []
name_pos = 0
phone_pos = 1
phone_header = [ 'Name', 'Phone Number']

def plaussibility(which):
    if not which.isdigit():
        print("\n Please enter a valid choice \n")
        return False
    which = int(which)
    if which <1 or which > len(phones):
        print("\n Please enter a valid choice \n")
        return False
    return True

def delete(which):
    if not plaussibility(which):
        return
    which = int(which)
    del phones[which-1]
    print("Deleted contact: ",which)
    
def save():
    file = open("myphones.csv","w", newline="")
    for item in phones:
        csv.writer(file).writerow(item)  ## whats writerow function??
    file.close()

    
def load():
    if os.access("myphones.csv",os.F_OK):
        loadfile = open("myphones.csv")
        for row in csv.reader(loadfile):
            phones.append(row)
        loadfile.close

def choice_menu():
    print("Choose on of the following options?")
    print("  s) Show")
    print("  n) New")
    print("  d) Delete")
    print("  e) Edit")
    print("  q) Quit")
    choice = input("Choice: ")
    if choice.lower() in ["s","n","d","e","q"]:
        return choice.lower()
    else:
        print(choice+"is an invalid choice. Please enter a valid choice")
    
    
def show():
    show_phone(phone_header, "")
    index = 1
    for phone in phones:
        show_phone(phone, index)
        index = index + 1
    print()
    
def show_phone(phone,index):
    phonetable = "{0:<3}  {1:<20}  {2:<16}"
    print(phonetable.format(index, phone[name_pos], phone[phone_pos]))

def edit(which):
    if not plaussibility(which):
        return
    which = int(which)
    
    phone = phones[which-1]
    print("Enter data for editing. Please press'enter' to leave it unchanged")
    
    newname = input("Enter new name: ")
    if newname == "":
        newname = phone[name_pos]
    
    newnum = input("Enter new number: ")
    if newnum == "":
        newnum = phone[phone_pos]
    phone = [newname,newnum]
    phones[which-1] = phone    
    
def create():
    print("Creating a new entry \n")
    new_name = input("Enter Name: ")
    new_num = input("Enter Number: ")
    phone = [new_name,new_num]
    phones.append(phone)
    print()
    
    
    
def main():
    load()
    
    while True:
        choice = choice_menu()
        if choice == None:
            continue
        if choice == "q":
            print("Exiting..")
            break
        elif choice == "d":
            which = input("which contact you wanto to delete: ")
            delete(which)
        elif choice == "n":
            create()
        elif choice == "s":
            show()
        elif choice == "e":
            which = input("which contact you want to edit: ")
            edit(which)
        else:
            print("Invalid option")
        
    save()
        
    
if __name__ == "__main__":
    main()
#%%