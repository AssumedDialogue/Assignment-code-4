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

CurrentBooks = {1: {"Title": "Harry Potter: the Goblet of fire", "Author": "J.K Rowling",
                             "Book ID": "98705381",
                             "Genre": "Fantasy"},
                      2: {"Title": "IT", "Author": "Stephen King",
                             "Book ID": "87015932",
                             "Genre": "Horror"},
                      3: {"Title": "The very Hungry Caterpillar", "Author": "Eric Carle",
                             "Book ID": "74028682",
                             "Genre": "Children Friendly"},
                      4: {"Title": "To Kill A mocking bird", "Author": "Harper Lee",
                             "Book ID": "00629611",
                             "Genre": "Gothic Fiction"},
                      5: {"Title": "Murder On Orient Express", "Author": "Agatha Christie",
                             "Book ID": "00003927",
                             "Genre": "Mystery Fiction",
                             },
                      }
 
 
class LibraryEncoder (json.JSONEncoder):
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
    NN = (1,2,3,4)
    MC = int(input( '\n' + "1. Search up a Book " + '\n' + "2. Add a new book " + '\n' + "3. Delete a book " + '\n' + "4. Edit a books information"))
    
    if MC == "1":
        read()
        break
    elif MC == "2":
        Create()
        break
    elif MC == "3":
        delete()
        break
    elif MC == "4":
        edit()
        break
    else:
        print("sorry u didnt choose a right option")
    
        
BookName = input("What is the title of your book?: ")
BookID = input("What is the ID Number of your book? (Must be 8 digits): ")
BookAuthor = input("What is the Authors name of your book?: ")



