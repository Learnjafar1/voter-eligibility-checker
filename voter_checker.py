def check_voter_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age >= 18:
            print("Congratulations, you can vote!")
        else:
            print("Sorry, you're too young.")
    except ValueError:
        print("Please enter a valid number.")

check_voter_eligibility()
