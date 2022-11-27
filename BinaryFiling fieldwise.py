import os
import struct

class StuRecord():
    def __init__(self):
        self.Id = 0
        self.Name = ""
        self.Class = ""
        self.Fee = 0.0
Student = StuRecord()
RECORDSTRUCTURE = 'i20s4sf'
RECORDSIZE = struct.calcsize(RECORDSTRUCTURE)
records = 0

def add():
    global records
    file = open("BinaryFile.dat", 'ab+')

    Student.Name = input("Enter your name here or leave blank to exit: ")
    while Student.Name != '':
        records += 1

        Student.Id = records
        Student.Class = input("Enter your class here: ")
        Student.Fee = float(input("Enter your fee here: "))

        data = struct.pack(RECORDSTRUCTURE, Student.Id, bytes(Student.Name, 'ascii'), bytes(Student.Class, 'ascii'), Student.Fee)
        file.write(data)
        Student.Name = input("Enter your name here or leave blank to exit: ")
    
    file.close()

def display():
    if records == 0:
            print("No data to display")
    try:
        file = open("BinaryFile.dat", 'rb')
        for i in range(records):
            file.seek(i* RECORDSIZE)
            data = file.read(RECORDSIZE)
            Student.Id, Student.Name, Student.Class, Student.Fee = struct.unpack(RECORDSTRUCTURE, data)

            print("ID is: ", Student.Id)
            print("Name is: ", Student.Name.decode())
            print("Class is: ", Student.Class.decode())
            print("Fee is: ", Student.Fee)
            print()
        file.close()
    except:
        print("File not found")
def search():
    global records
    found = False
    SearchID = int(input("Enter a id to search: "))
    try:
        file = open("BinaryFile.dat", 'rb')
        for i in range(records):
            file.seek(i* RECORDSIZE)
            data = file.read(RECORDSIZE)
            Student.Id, Student.Name, Student.Class, Student.Fee = struct.unpack(RECORDSTRUCTURE, data)

            if Student.Id == SearchID:
                found = True
                print("ID is: ", Student.Id)
                print("Name is: ", Student.Name.decode())
                print("Class is: ", Student.Class.decode())
                print("Fee is: ", Student.Fee)
                print()
        if found is False:
            print("SearchId not found")
        file.close()
    except:
        print("File not found")

def delete():
    ID = int(input("Enter the id you want to delete: "))
    global records
    deletedList = []
    deleted = False
    try:
        file = open("BinaryFile.dat", 'rb')
        for i in range(records):
            file.seek(i* RECORDSIZE)
            data = file.read(RECORDSIZE)
            Student.Id, Student.Name, Student.Class, Student.Fee = struct.unpack(RECORDSTRUCTURE, data)

            if ID != int(Student.Id):
                deletedList.append(data)
            else:
                deleted = True
                records -= 1
        file.close()
    
        if deleted is False:
            print("Deleted Id not found")
        else:
            file = open("BinaryFile.dat", 'wb')
            for i in range(len(deletedList)):
                file.write(deletedList[i])
            file.close()
        
    except Exception as e:
        print(e)
        #print("File not found")

def edit():
    ID = int(input("Enter the id you want to edit: ")) - 1
    try:
        file = open("BinaryFile.dat", 'rb+')
        file.seek(ID* RECORDSIZE)
        data = file.read(RECORDSIZE)
        Student.Id, Student.Name, Student.Class, Student.Fee = struct.unpack(RECORDSTRUCTURE, data)

        StuNAME = input("Enter a new name to update: ")
        StuCLASS = input("Enter a new class to update: ")
        StuFEE = float(input("Enter a new fee to update: "))
        data = struct.pack(RECORDSTRUCTURE, Student.Id, bytes(StuNAME, 'ascii'), bytes(StuCLASS, 'ascii'), StuFEE)

        file.seek(ID* RECORDSIZE)
        file.write(data)
        file.close()
        print("Record updated")
    except:
        print("File not found")

def options():
    print("1. Add record wise ")
    print("2. Read record wise.")
    print("3. Search record wise.")
    print("4. Delete record wise.")
    print("5. Edit record wise.")
    print("0. Quit.")
    opt = int(input("Enter the choice... "))
    return opt

#main program
try:
    file = open("BinaryFile.dat", 'rb')
    file.seek(0, os.SEEK_END)
    FileSize = file.tell()
    records = int(FileSize/ RECORDSIZE)
    file.close()
except:
    records = 0
opt = options()
while opt != 0:
    if opt == 1: add()
    if opt == 2: display()
    if opt == 3: search()
    if opt == 4: delete()
    if opt == 5: edit()
    opt = options()