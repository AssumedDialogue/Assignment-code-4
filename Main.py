###############
#Name: Areeba Minhaj
#Date 12/08/2022
#class: intro to programming principles
################

import json
 
f=open(Areeba.json)
 

def Create():
    with open(Areeba.json,'r') as f:
        temp = json.load(f)
    
    NewBook={}
    NewBook["Title"] = input("Enter New Book title: ")
    if NewBook["Title"] not in Areeba.keys():
        NewBook["Author"] = input("Enter the Author of the book: ")
        NewBook["BookId"] = input("Enter the book ID number: ") #WHILE LOOPP
        NewBook["Genre"] = input("Enter the Genre of book: ")
        temp.append(NewBook)
        with open(Areeba,'w') as f:
            json.dump(temp, f ,indent=4)


def Delete():
    with open(Areeba.json,'r') as f:
        temp = json.load(f)
    print(temp)
    UserBook=[]
    UserBook["Title"] = input("Enter the Book title you want to delete: ")
    print("Enter The title of The book Which You Want To Delete :- ")
    temp = input()
    if temp in Areeba.keys():
        Areeba.pop(temp)  # here we are removing that particular data
        print("Book "+str(temp)+" iss Deleted")
    else:
        print("Invalid Book")
    with open(Areeba,'w') as f:
        json.dumps(Areeba)


def Read():
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
    print("Enter The Book Title of The Product Which You Want To Update: ")
    UT = input()
     
    if UT in Areeba.keys():
        print()
        q = int(input("Want to update the whole Book data Enter '0' else '1' for specific information : "))
         
        if (q == 0):
            
            Title = input("Enter Book Title: ")
            Author = input("Enter the Author of the book: ")
            BookId = input("Enter the book ID number (must be 8 Digits): ") #WHILE LOOPP
            Genre = input("Enter the Genre of book: ")
            Areeba[UT] = {'Title': Title, 'Author': Author,'BookId': BookId, 'Genre': Genre,}
            
            z = int(input("Please Press '0' to Add more Attributes/Properties of Product or Press '1' to Continue: "))
             
            if(z == 0):
                print("Enter Number of New Attributes/Properties of Product :- ")
                n = int(input())
                for i in range(n):
                    nam = input("Enter Attribute Name That you Want To Add :- ")
                    pro = input("Enter The "+str(nam)+" of Product :- ")
                    Areeba[UT][nam] = pro
            print("The Book "+str(UT)+" is Updated Successfully")
             
        elif(q == 1):
            print("Enter Which Attribute of Product You want to Update :- ")
            p = input()
             
            if p in Areeba[UT].keys():
                u = input("Enter "+str(p)+" of Product :- ")
                Areeba[UT][p] = u
                print("Product ID "+str(UT)+"'s attribute " +
                      str(p)+" is Updated Successfully...!!!")
            else:
                print("Invalid Product Attribute...!!!")
        else:
            print("Invalid Choice...!!!")
    else:
        print("Invalid Product ID...!!!")
    json.dumps(Areeba)


print("Welcome to the Library!" + '\n' + "What would you like to do?" )

while True:
    NN = (1,2,3,4)
    MC = int(input( '\n' + "1. Search up a Book " + '\n' + "2. Add a new book " + '\n' + "3. Delete a book " + '\n' + "4. Edit a books information"))
    
    if MC == 1:
        Read()
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



