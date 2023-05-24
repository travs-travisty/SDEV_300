import re

def validate_age(age):
    try:
        age = int(age)
        if age >= 18 and age <= 120:
            return True
        else:
            print("Invalid age. You must be at least 18 years old to register.")
            return False
    except ValueError:
        print("Invalid age. Please enter a valid number.")
        return False

def validate_state(state):
    valid_states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID",
        "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
        "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
        "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV",
        "WI", "WY"
    ]
    if state.upper() in valid_states:
        return True
    else:
        print("Invalid state. Please enter a valid two-letter state code.")
        return False

def validate_zipcode(zipcode):
    if re.match(r"^\d{5}$", zipcode):
        return True
    else:
        print("Invalid zipcode. Please enter a valid 5-digit zipcode.")
        return False

def register_voter():
    print("=== Voter Registration ===")

    # Prompt for user details
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    age = int(input("Age: "))  # Convert input to integer
    country = input("Country of Citizenship: ")
    state = input("State of Residence: ")
    zipcode = input("Zipcode: ")

    # Validate age
    if not validate_age(age):
        return

    # Validate state
    if not validate_state(state):
        return

    # Validate zipcode
    if not validate_zipcode(zipcode):
        return

    # Check eligibility
    if age >= 18 and country.lower() == "us":
        print("Congratulations! You are eligible to vote.")

        # Additional questions for eligible voters
        print("Additional Questions:")
        # Add additional questions here
        
        # Print registration summary
        print("\nRegistration Summary:")
        print("Name:", first_name, last_name)
        print("Age:", age)
        print("Country of Citizenship:", country)
        print("State of Residence:", state)
        print("Zipcode:", zipcode)
    else:
        print("You are not eligible to vote.")

register_voter()
