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
RecordSize = struct.calcsize(RECORDSTRUCTURE)

file = open("BinaryFile.dat", 'ab+')
file.seek(0, os.SEEK_END)
FileSize = file.tell()
NoOfRecords =  int(FileSize / RecordSize)

Student.Id = NoOfRecords + 1
Student.Name = input("Enter your name here: ")
Student.Class = input("Enter your class here: ")
Student.Fee = float(input("Enter your fee here: "))

data = struct.pack(RECORDSTRUCTURE, Student.Id, bytes(Student.Name, 'ascii'), bytes(Student.Class, 'ascii'), Student.Fee)
file.write(data)
file.close()


file = open("BinaryFile.dat", 'rb')
file.seek(0, os.SEEK_END)
FileSize = file.tell()
NoOfRecords =  int(FileSize / RecordSize)
for i in range(NoOfRecords):
    file.seek(i* RecordSize)
    data = file.read(RecordSize)
    Student.Id, Student.Name, Student.Class, Student.Fee = struct.unpack(RECORDSTRUCTURE, data)

    print("ID is: ", Student.Id)
    print("Name is: ", Student.Name.decode())
    print("Class is: ", Student.Class.decode())
    print("Fee is: ", Student.Fee)
    print()
file.close()