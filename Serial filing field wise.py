import os
def add():
    file = open("StFile.txt", "at" )
    Sname =input("Enter students name or Enter nothing to end: ")
    while Sname != "":
        Sclass =input("Enter students class: ")
        Sfee =input("Enter students fee: ")
        file.write(Sname + "\n")
        file.write(Sclass + "\n")
        file.write(str(Sfee) + "\n")

        Sname =input("Enter students name or Enter nothing to end: ")
    file.close()

def display():
    try:
        file = open("StFile.txt", "rt" )
        Sname = file.readline()
        while Sname != "":
            Sclass = file.readline()
            Sfee = file.readline()
            print(Sname , end ="")
            print(Sclass , end ="")
            print(Sfee)
            Sname = file.readline()
        file.close()
    except:
        print("File doeen't exists")

def search():
    found = False
    try:
        file = open("StFile.txt", "rt" )
        name =input("Enter Name to search: ")
        Sname = file.readline()
        while Sname != "":
            Sclass = file.readline()
            Sfee = file.readline()
            if Sname.strip() == name:
                found = True
                print(Sname , end ="")
                print(Sclass , end ="")
                print(Sfee)
            Sname = file.readline()
        if found is False:
            print(name , " doesn't exists")
        file.close()
    except:
        print("File doesn't exists")

def delete():
    deleted = False
    try:
        file = open("StFile.txt", "rt" )
        tempfile = open("tempFile.txt", "at")
        name =input("Enter Name to delete: ")
        Sname = file.readline()
        while Sname != "":
            Sclass = file.readline()
            Sfee = file.readline()
            if Sname.strip() != name:
                tempfile.write(Sname)
                tempfile.write(Sclass)
                tempfile.write(Sfee)  
            else:
                deleted = True
            Sname = file.readline()
        if deleted is False:
            print(name , " doesn't exists")
        tempfile.close()
        file.close()
        os.remove("StFile.txt")
        os.rename("tempFile.txt","StFile.txt")
    except:
        print("File doesn't exists")

def edit():
    edited = False
    try:
        file = open("StFile.txt", "rt" )
        tempfile = open("tempFile.txt", "at")
        name =input("Enter Name to edit: ")
        Sname = file.readline()
        while Sname != "":
            Sclass = file.readline()
            Sfee = file.readline()
            if Sname.strip() == name:
                edited = True
                stname = input("ENTER NEW NAME TO UPDATE: ")
                stclass = input("ENTER NEW CLASS TO UPDATE: ")
                stfee = input("ENTER NEW FEE TO UPDATE: ")
                tempfile.write(stname + "\n")
                tempfile.write(stclass+ "\n")
                tempfile.write(stfee)  
            else:
                tempfile.write(Sname)
                tempfile.write(Sclass)
                tempfile.write(Sfee)  
            Sname = file.readline()
        if edited is False:
            print(name , " doesn't exists")
        tempfile.close()
        file.close()
        os.remove("StFile.txt")
        os.rename("tempFile.txt","StFile.txt")
    except:
        print("File doesn't exists")

def options():
    print("Enter 1 to add into file.")
    print("Enter 2 to view into file.")
    print("Enter 3 to search from file.")
    print("Enter 4 to delete from file.")
    print("Enter 5 to edit from file.")
    print("Enter 0 to quit.")
    opt = int(input("Enter your choice here....... "))
    return opt

#Main
opt = options()
while opt != 0:
    if opt == 1 : add()
    if opt == 2 : display()
    if opt == 3 : search()
    if opt == 4 : delete()
    if opt == 5 : edit()
    opt = options()