import lista_modulo as lm

def options_action(option):
    if option == 1:
        lm.m1_create_list_menu()
    elif option == 2:
        lm.m2_view_list_menu()
    elif option == 3:
        lm.m3_udpdate_list_menu()
    elif option == 4:
        lm.m4_add_element()
    elif option == 5:
        lm.m5_remove_element()
    elif option == 6:
        lm.m6_sort_asc()
    elif option == 7:
        lm.m7_sort_des()
    elif option == 8:
        lm.m8_search_element()
    else:
        lm.menu()

def app():
    finish_program = False
    lm.menu()
    while not finish_program:
        try:
            option = int(input(">>> Select a Menu Option: "))
            if option < 1 or option > 10:
                raise Exception ("Invalid Option.")
            elif option != 10:
                options_action(option)
            else:
                finish_program = True
        except ValueError:
            print("Please enter an option number.")
        except Exception as error:
            print(error)

app()
