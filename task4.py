"""
4)Write a Python functiom to validate the Regular Expression for the following:
a) Email Address
b) Mobile numbers of Bangladesh
c) Telephone numbers of USA
d) 16 character Alpha-Numeric password composed of  alphabets of Upper Case, Lower Case, Special Characters, Numbers
"""

# a) Email Address:

# Importing  the regular expression module
import re
#Defining a function to validate the email address
def validate_email(email):
    # Regular expression pattern for validating email addresses
    pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,}$"

    # Use re.search() to find a match to the pattern in the email
     # If a match is found
    if re.search(pattern,email):
        # Return True indicating the email address is valid
        return True
    
    # If no match is found
    else:
        # Return False indicating the email address is invalid
        return False
    
# Example email address to validate
email="example@gmail.com"

# If the email address is valid
if validate_email(email):
    # Print the validation result
    print(f"Valid email address: {email}")
# If the email address is invalid
else:
    # Print the validation result
    print(f"Invalid email address: {email}")


# b) Mobile numbers of Bangladesh

#Defining afunction to validate the mobile number
def validate_bangladesh_mobile_number(mobile_number):
    
    # Regular expression pattern for validating Bangladesh mobile numbers
    pattern=r"^01[3-9]\d{8}$"

    # Use re.search() to find a match to the pattern in the mobile number
    # If a match is found
    if re.search(pattern,mobile_number):
        # Return True indicating the mobile number is valid
        return True
    
    # If no match is found
    else:
        # Return False indicating the mobile number is invalid
        return False

# Example Bangladesh mobile number to validate
mobile_number="01712345678"
# If the mobile number is valid
if validate_bangladesh_mobile_number(mobile_number):
    # Print the validation result
    print(f"Valid Bangladesh mobile number {mobile_number}")

# If the mobile number is invalid
else:
    # Print the validation result
    print(f"Invalid Bangladesh mobile number {mobile_number}")


# c) Telephone numbers of USA

# Defining a function to validate the telephone number
def validate_USA_telephone_number(telephone_number):

# Regular expression pattern for validating USA telephone numbers
    pattern=r"^\+1\d{10}$"

    # If a match is found
    if re.search(pattern,telephone_number):
        # Return True indicating the telephone number is valid
        return True
    
    # If no match is found
    else:
        # Return False indicating the telephone number is invalid
        return False
    
# Example USA telephone number to validate
telephone_number="+12345678901"

# If the telephone number is valid
if validate_USA_telephone_number(telephone_number):
    # Print the validation result
    print(f"Valid USA telephone number {telephone_number}")

# If the telephone number is invalid
else:
    # Print the validation result
    print(f"Invalid USA telephone number {telephone_number}")


# d) 16 character Alpha-Numeric password composed of  alphabets of Upper Case, Lower Case, Special Characters, Numbers

# Defining a function to validate the password 
def validate_passowrd(password):

    # Regular expression pattern for validating 16-character Alpha-Numeric passwords with specific c
    pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{16}$"
    
     # Use re.search() to find a match to the pattern in the password
     # If a match is found
    if re.search(pattern,password):
        # Return True indicating the password is valid
        return True
    
    # If no match is found
    else:
        # Return False indicating the password is invalid
        return False
    
# Example password to validate
password="Abc@123456789012"
# If the password is valid
if validate_passowrd(password):
    # Print the validation result
    print(f"Valid password {password}")

# If the password is invalid
else:
    # Print the validation result
    print(f"Invalid password {password}")




