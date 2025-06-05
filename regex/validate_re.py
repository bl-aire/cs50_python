import re

email = input("Enter your email: ").strip()

# .+ || ..*
# r"" needed here because we are using \ to escape . in .edu
# r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$"
# lower() can be used to fix case sensitivity of email
# ? means zero or one repetition so the parenthesis is optional

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov)$", email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")