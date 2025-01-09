#Data Types in Python
'''
#Primitive Data Types in Python
#1. Numbers
Integer = 6
Float = 6.0
Complex = 1+2j
print(type(Integer))
print(type(Float))
print(type(Complex))

#2. Boolean
Boolean = True
print(type(Boolean))
Boolean = False
print(type(Boolean))

#3. Strings -> bisa indexing & slicing -> immutable
String = 'Naufal'
print(type(String))
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""
print(multi_line)
name = "Naufal Yoga"
print(f"Hello, nama saya {name}") #Formmated String
print("Nama saya %s" % (name)) #%-formatting
print("Nama saya {}".format(name)) #str.format()
'''

#Collection Data Type
#1. List -> mutable -> bisa indexing
list = [1, 2.2, 'naufal']
print(type(list))

exList = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(exList[0])
print(exList[2])
print(exList[-1])
print(exList[-3])
print(exList[0:5:2])
print(exList[1:])
print(exList[:3])

#2. Tuple -> immutable -> bisa indexing
Tuple = (1, "naufal", 1+3j)
print(type(Tuple))

#3. Set -> immutable -> tidak bisa indexing
Set = {1, 2, 7, 2, 3, 13, 3}
print(Set)
print(type(Set))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
print("Union:", union)
intersection = set1.intersection(set2)
print("Intersection:", intersection)

#4. Dictionary -> mutable -> tidak bisa indexing (gunakan key-nya)
Dictionary = { 'name': 'Naufal Yoga', 'age': 20, 'isMarried': False }
print(Dictionary ['name'])
