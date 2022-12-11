###############
#Name: Areeba Minhaj
#Date 12/08/2022
#class: intro to programming principles
################

import json
try:
    Areeba = (r"C:\Users\minha\Assignment code 4\Areeba.json")
except FileNotFoundError:
    print('File not available')
 

def Create():
    with open(Areeba.json,'r') as f:
        temp = json.load(f)
    
    NewBook={}
    NewBook["Title"] = input("Enter New Book title: ")
    if NewBook["Title"] not in Areeba.keys():
        NewBook["Author"] = input("Enter the Author of the book: ")
        NewBook["BookId"] = input("Enter the book ID number: ") 
        NewBook["Genre"] = input("Enter the Genre of book: ")
        temp.append(NewBook)
        with open(Areeba,'w') as f:
            json.dump(temp, f ,indent=4)


def Delete():
    with open(Areeba.json,'r') as f:
        temp = json.load(f)
    temp = input("Enter The info you'd like to delete: ")
    while True:
        if temp in Areeba.keys():
            Areeba.pop(temp)
            print("Book info "+str(temp)+" is Deleted")
            break
        else:
            print("Invalid Book")
    with open(Areeba,'w') as f:
        json.dumps(Areeba)


def Display():
    with open (Areeba,'r') as f:
        temp = json.load(f)
        i =1
        for D in temp:
            Title= D["Title"]
            Author= D["Author"]
            BookId= D["BookId"]
            Genre= D["Genre"]
            print(f"Book Number: {i}"+'\n'+ f"Book Title: {Title}"+'\n'+ f"Book Author: {Author}"+'\n'+ f"Book Book ID: {BookId}"+'\n'+ f"Book Genre: {Genre}")
            i=+ 1

       
def Edit():
    with open (Areeba,'r') as f:
        temp = json.load(f)
    UT = input("Enter The Book Title of the book You Want To edit: ")

    while True: 
        if UT in Areeba.keys():
            print()
            b = int(input("Want to update the all of the Books data Enter '0' else '1' for specific information : "))
         
            if (b == 0):
            
                Title = input("Enter Book Title: ")
                Author = input("Enter the Author of the book: ")
                BookId = input("Enter the book ID number: ")
                Genre = input("Enter the Genre of book: ")
                Areeba[UT] = {'Title': Title, 'Author': Author,'BookId': BookId, 'Genre': Genre,}
                print("The Book "+str(UT)+" is Updated Successfully")
                break

              
            elif(b == 1):
                d = input("Enter Which information of the Book You want to Update: ")

                while True:
                    if d in Areeba[UT].keys():
                       u = input("Enter "+str(d)+" of book : ")
                       Areeba[UT][d] = u
                       print("Product ID "+str(UT)+"'s attribute " + str(d)+" is Updated Successfully...!!!")
                       break
                    else:
                        print("wrong book Attribute")
                break        
            else:
                print("wrong option chosen")
        else:
            print("Can't find Book in library ")
        json.dumps(Areeba)


print("Welcome to the Library!" + '\n' + "What would you like to do?" )

while True:
    NN = (1,2,3,4)
    MC = int(input( '\n' + "1. Display current library " + '\n' + "2. Add a new book " + '\n' + "3. Delete a information " + '\n' + "4. Edit a books information"))
    
    if MC == 1:
        Display()
        break
    elif MC == 2:
        Create()
        break
    elif MC == 3:
        Delete()
        break
    elif MC == 4:
        Edit()
        break
    else:
        print("sorry u didnt choose a right option")



