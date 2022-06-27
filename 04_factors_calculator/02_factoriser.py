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

            

# gets factors, returns a sorted list
def get_factors(num):
    print("The factors of",num,"are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
