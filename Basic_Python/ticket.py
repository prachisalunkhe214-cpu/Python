has_ticket = True
has_id = False

# Both must be True
if has_ticket and has_id:
    print("Allowed entry.")
else:
    print("Access denied.")  # Runs because has_id is False

# Only one needs to be True
if has_ticket or has_id:
    print("Welcome inside!")  # Runs because has_ticket is True
