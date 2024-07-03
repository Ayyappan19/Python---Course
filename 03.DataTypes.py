# DataTypes

# 01.Int
a = 10 
print("value : ", a)
print(type(a))

print("\n")

# 02.Float
a = 10.50 
print("value : ", a)
print(type(a))

print("\n")

# 03.Boolean
a = True
print("value : ", a)
print(type(a))

print("\n")

# 04.Complex
a = 5 + 8j
print("value : ", a)
print(type(a))

print("\n")

# 05.String
a = 'Hello'
print("value : ", a)
print(type(a))

a = "Hello"
print("value : ", a)
print(type(a))

print("\n")

# 06.List
a = [1,2,3,4,5]
print("value : ", a)
print(type(a))

print("\n")

# 07.Set
a = {1,2,3,4,5}
print("value : ", a)
print(type(a))

a = {1,2,4,5,3,4,5}
print("value : ", a)
print(type(a))

a = {"ram","sam","mam","sam"}
print("value : ", a)
print(type(a))


print("\n")

# 08. Tuple
a = (1,2,3,4,5)
print("value : ", a)
print(type(a))

print("\n")

# 09.Range
a = range(10)
print("value : ", a)
print(type(a))

print(list(range(10)))
print(list(range(0,20,2)))

print("\n")

# 10.Dictionary
a = {"Ram":"10","ak":"20"}
print("value : ", a)
print(type(a))
dic = a.keys()
print(dic)

dic = a.values()
print(dic)

print(a["ak"])
print(a.get("ak"))