###############
#Name: Areeba Minhaj
#Date 12/08/2022
#class: intro to programming principles
################

import json

class Librabry:
    def __init__(self, BookName, BookID, BookAuthor):
        self.name = BookName
        self.Id = BookID
        self.Author = BookAuthor
 
class create:
    def bleh():
        print()

class delete:
    def bleh():
        print()

class read():
    def bleh():
        print()

class edit():
    def nleh():
        print()

print("Welcome to the Library!" + '\n' + "What would you like to do?" )
while True:
    try:
        NN = ("1","2","3","4")
        MC = input( '\n' + "1. Search up a Book " + '\n' + "2. Add a new book " + '\n' + "3. Delete a book " + '\n' + "4. Edit a books information")
        if MC in NN:
            raise MyException
    except MyException:
        print("Enter a valid option")
        break
        
    

BookName = input("What is the title of your book?: ")
BookID = input("What is the ID Number of your book? (Must be 8 digits): ")
BookAuthor = input("What is the Authors name of your book?: ")
if MC == "1":
    Book = read(BookName,BookID, BookAuthor)
elif MC == "2":
    Book = create(BookName,BookID, BookAuthor)
elif MC == "3":
    Book = delete(BookName,BookID, BookAuthor)
elif MC == "4":
    Book = edit(BookName,BookID, BookAuthor)

