# Removes whitespace
email = input("Enter your email: ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Validated email")
else:
    print("Invalid email")