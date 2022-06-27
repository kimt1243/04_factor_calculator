#checks input is a number more tham zero
def num_check(question, num):
    valid = False
    while not valid:

        error = "Please enter a integer that is more than or equal to 1, and less than or equal to 200"
      

        try:

            response = int(input(question))

            if 0 < response < 201:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)


#Main Routine goes here


keep_going =""
while keep_going == "": 
    print()
    # ask user for an integer (must be more than 1)
    var_integer = num_check("Enter an integer: ", 1)
    print()