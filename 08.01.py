username, password = "Andrius", "Slaptaszodis"

while 1:
    test_username = input("Enter username: ")
    test_password = input("Enter password: ")
    if username == test_username and password == test_password:
        print("Sveiki, jus prisijungete prie matricos")
        break
    else:
        print("\nBandykite dar karta!\n")
