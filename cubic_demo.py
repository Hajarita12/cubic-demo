# cubic_demo.py
def greet_user(name):
    print("Hello, " + name + "!")

def add_numbers(a, b):
    return a + b

def main():
    user_name = input("Enter your name: ")
    greet_user(user_name)
    
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    result = add_numbers(x, y)
    print("Sum:", result)

if __name__ == "__main__":
    main()
