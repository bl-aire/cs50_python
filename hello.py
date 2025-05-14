# Ask user for name
name = input("What is your name?")

# Greet user
# Format string f""
print(f"Hello, {name}!")
print("Hello,", name)
print("Hello, " + name)

# Override default value of end in print method
# print(*objects, sep='', end= '\n', file=sys.stdout, flush=False)
print("Hello, ", end="" )
print(name)

# Escaping
print('Hello, "friend"')
print("Hello, \"friend\"")