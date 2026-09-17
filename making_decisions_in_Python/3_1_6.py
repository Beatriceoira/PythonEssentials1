while True:
    n = int(input("Enter a number: "))
    print(n >= 100)

    reset = input("Reset? (y/n): ").lower()
    if reset != "y":
        break
