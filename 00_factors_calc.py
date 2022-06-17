# Function go here

# Puts series of symbols at start and end of text
def statement_generator(text, decoration):

    # Make string with five chracters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose an integer that is more than or equal to 1 and less or equal to 200")
    print()
    print("This programme calculates if the integer is a UNITY, Prime number or a Perfect square")
    print()
    print("The program will list all the factors of the integer")
    print()

    return""

# checks input is a number more than a given value
def num_check(question):
    valid = False
    while not valid:


        error = "Please enter a integer that is more than or equal to 1, and less than or equal to 200"
      

        try:


            response = int(input(question))

            if 0 < response < 200:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)


# gets factors, returns a sorted list
def get_factors(x):

    factors = []

    print("The factors of",x,"are: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print()
            factors.append(i)
            return factors


# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ")

    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        comment = "One is UNITY! It only has one factor.  Itself :)"
        factor_list = ""

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
        factor_list = ""

    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)
        factor_list = ""
        
        
    # ouput factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
























