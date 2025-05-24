# this will be our main file

def foo_function():
    print("This is an extra function that can be used in other modules.")

def main():
    print("This is the main function.")
    print("You can run this script directly or import it as a module.")

if __name__ == "__main__":
    print("Hello, World!")
    main()
    foo_function()