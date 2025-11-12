Book1 = {
    'Name':' The Hiding Place',
    'id': " 26484639",
    'Date published': ' 1942',
    'Status': ' Available',
    'Type': ' Christian biography'
}

Book2 = {
    'Name':' The Last Raid',
    'id': " 5738973487",
    'Date published': ' 1986',
    'Status': ' Unavailable',
    'Type': ' Information'
}

Book3 = {
    'Name':' Hitler: The Dictator',
    'id': " 26484639",
    'Date published': ' 1942',
    'Status': ' Available',
    'Type': ' Christian biography'
}

Book4 = {
    'Name':' Amy Carmicheal',
    'id': " 547879645",
    'Date published': '2031',
    'Status': 'Available',
    'Type': 'Christian biography'
}

Books = ("""
1.) The Hiding Place
2.) The Last Raid
3.) Hitler: The Dictator
4.) Amy Carmicheal
""")


print(Books)
customer = input("Hello what book would you like to borrow: ")

if customer == "1":
    options = ("""
    1.) Borrow Book
    2.) About the book
    3.) Cancle
    """) 
    print(options)
    response1 = input("What would you like to do with this book: ")
    if response1 == "1":
        number = ("Input Phone number: ")
        print("Pls bring the book back in two weeks or you will be fined.")
    if response1 == "2":
        for x,y in Book1.items():
            print(f"{x}:{y}")
    if response1 == "3":
        print("Thank you for comming")
if customer == "2":
    options = ("""
    1.) Borrow Book
    2.) About the book
    3.) Cancle
    """) 
    print(options)
    response1 = input("What would you like to do with this book: ")
    if response1 == "1":
        number = ("Input Phone number: ")
        print("Pls bring the book back in two weeks or you will be fined.")
    if response1 == "2":
        for x,y in Book2.items():
            print(f"{x}:{y}")
    if response1 == "3":
        print("Thank you for comming")
if customer == "3":
    options = ("""
    1.) Borrow Book
    2.) About the book
    3.) Cancle
    """) 
    print(options)
    response1 = input("What would you like to do with this book: ")
    if response1 == "1":
        number = ("Input Phone number: ")
        print("Pls bring the book back in two weeks or you will be fined.")
    if response1 == "2":
        for x,y in Book3.items():
            print(f"{x}:{y}")
    if response1 == "3":
        print("Thank you for comming")
if customer == "4":
    options = ("""
    1.) Borrow Book
    2.) About the book
    3.) Cancle
    """) 
    print(options)
    response1 = input("What would you like to do with this book: ")
    if response1 == "1":
        number = ("Input Phone number: ")
        print("Pls bring the book back in two weeks or you will be fined.")
    if response1 == "2":
        for x,y in Book4.items():
            print(f"{x}:{y}")
    if response1 == "3":
        print("Thank you for comming")


