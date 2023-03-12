import os
import struct

RECORDSTRUCTURE = '10si'
class record():
    def __init__(self):
        self.name = ""
        self.age = 0
person = record()
recordSize = struct.calcsize(RECORDSTRUCTURE)


file = open('File.dat', 'ab+')
file.seek(0, os.SEEK_END)
fileSize = file.tell()
records = int(fileSize / recordSize)

for i in range(4):
    person.name = input("Enter a name: ")
    person.age = int(input("Enter a age: "))
    data = struct.pack(RECORDSTRUCTURE, bytes(person.name, ('ascii')), person.age)
    file.write(data)
file.close()

file = open('File.dat', 'rb')
file.seek(0, os.SEEK_END)
fileSize = file.tell()
records = int(fileSize / recordSize)
for i in range(records):
    file.seek(i * recordSize)
    data = file.read(recordSize)
    person.name , person.age = struct.unpack(RECORDSTRUCTURE, data)
    print("Name is: ", person.name.decode())
    print("Age is: ", person.age)
    print()
file.close()