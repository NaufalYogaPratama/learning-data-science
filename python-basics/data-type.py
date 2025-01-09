#Data Types in Python

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