import re
import tkinter as tk
from tkinter import messagebox

def validate_age(age):
    try:
        age = int(age)
        if age >= 18 and age <= 120:
            return True
        else:
            messagebox.showerror("Error", "Invalid age. You must be at least 18 years old to register.")
            return False
    except ValueError:
        messagebox.showerror("Error", "Invalid age. Please enter a valid number.")
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
        messagebox.showerror("Error", "Invalid state. Please enter a valid two-letter state code.")
        return False

def validate_zipcode(zipcode):
    if re.match(r"^\d{5}$", zipcode):
        return True
    else:
        messagebox.showerror("Error", "Invalid zipcode. Please enter a valid 5-digit zipcode.")
        return False

def register_voter():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    age = entry_age.get()
    country = entry_country.get()
    state = entry_state.get()
    zipcode = entry_zipcode.get()

    if not validate_age(age):
        return
    if not validate_state(state):
        return
    if not validate_zipcode(zipcode):
        return

    if age >= 18 and country.lower() == "us":
        messagebox.showinfo("Success", "Congratulations! You are eligible to vote.")
        # Additional questions for eligible voters
        # Add additional questions here

        summary = (
            "Name: " + first_name + " " + last_name + "\n" +
            "Age: " + str(age) + "\n" +
            "Country of Citizenship: " + country + "\n" +
            "State of Residence: " + state + "\n" +
            "Zipcode: " + zipcode
        )
        messagebox.showinfo("Registration Summary", summary)
    else:
        messagebox.showinfo("Not Eligible", "You are not eligible to vote.")

# Create GUI window
window = tk.Tk()
window.title("Voter Registration")

# Create labels and entry fields
label_first_name = tk.Label(window, text="First Name:")
label_first_name.pack()
entry_first_name = tk.Entry(window)
entry_first_name.pack()

label_last_name = tk.Label(window, text="Last Name:")
label_last_name.pack()
entry_last_name = tk.Entry(window)
entry_last_name.pack()

label_age = tk.Label(window, text="Age:")
label_age.pack()
entry_age = tk.Entry(window)
entry_age.pack()

label_country = tk.Label(window, text="Country of Citizenship:")
label_country.pack()
entry_country = tk.Entry(window)
entry_country.pack()

label_state = tk.Label(window, text="State of Residence:")
