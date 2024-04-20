list_is_created = False
number_list = []

def menu():
    print("""
===============================================
Main Menu:
1. Create a list
2. View List Data
3. Update a List Element
4. Add a List Element
5. Remove a List Element
6. Sort List in Ascending Order
7. Sort List in Descending Order
8. Search Element
9. Return to Main Menu
10. Exit     
===============================================      
""")

"""MENU 1"""
def m1_create_list_menu():
    print("""
===============================================
(1) CREATE A LIST:
===============================================
1. Create a list manually: 
2. Enter a number of elements to create a random list: 
""")
def m1_create_list_manually():
    print("Enter all the number you wish to add to the list. \nTo end, enter 'END'")
    conditional = True
    while conditional:
        try:
            text_input = input("Enter a number: ")
            if text_input.upper() == 'END':
                conditional = False
            else:
                number = float(text_input)
                number_list.append(number)
        except Exception:
            print("There was an entry error. Try again.")
    
def m1_create_random_list():
    conditional = True
    while conditional:
        try:
            length_list = int(int("Enter the number of elements in the list to create: "))
            if length_list <= 0:
                raise Exception("Incorrect Value.")
            else:
                conditional = False
                #completar
        except ValueError:
            print("There was an entry error. Try again.")

"""MENU 2"""
def m2_view_list_menu():
    print("""
===============================================
(2) VIEW LIST DATA:
===============================================
1. Enter option 1 of 2: 
2. Enter option 2 of 2: 
""")
def m2_view_list():
    print("Menu 2")



"""MENU 3"""
def m3_udpdate_list_menu():
    print("""
===============================================
(3) UPDATE A LIST ELEMENT:
===============================================
1. Add an element at the end of the list: 
2. Add an element at a specific position:
""")
def m3_update_list():
    print("Menu 3")



"""MENU 4"""
def m4_add_element_menu():
    print("""
===============================================
(4) ADD A LIST ELEMENT:
===============================================
1. Add an element at the end of the list: 
2. Add an element at a specific position:
""") 
def m4_add_element():
    print("Menu 4")





"""MENU 5"""
def m5_remove_element_menu():
    print("""
===============================================
(5) REMOVE A LIST ELEMENT:
===============================================
1. Remove an element by entering its value: 
2. Remove an element by its index position (Starting "0" from the left):  
""") 
def m5_remove_element():
    print("Menu 5")

def m6_sort_asc():
    print("Menu 6")

def m7_sort_des():
    print("Menu 7")

def m8_search_element():
    print("Menu 8")
