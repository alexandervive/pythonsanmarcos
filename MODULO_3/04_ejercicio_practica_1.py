#Programa

conditional = True
number_list = []

while conditional:
    try:
        number_input = input("Enter a digit: ")
        if number_input.upper() == "END":
            conditional = False
        else:
            number = int(number_input)
            number_list.append(number)
    except ValueError:
        print("Please enter a digit.")

print(f""""
Highest Number Found: {max(number_list)}
Lowest Number Found: {min(number_list)}""")