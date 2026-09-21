# Accept PAN number from the user
pan = input("Enter PAN Number: ")

# Regular expression for PAN format: AAAAA9999A
pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

# Validate PAN number 
if re.match(pattern, pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")
