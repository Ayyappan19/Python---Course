"""
Dictionary Function

Key()
Values()
Get()
Items()
Clear()
Copy()
Pop()
Update()

"""

print("Dictionary")
first = {"Name":"Ayyappan","Age":"23"}
print(first)


# 01.Keys()

print("Keys")
key = first.keys()
print(key)

print("\n")

# 02.Values()

print("Values")
value = first.values()
print(value)

print("\n")

# 03.Get()

print("Get :")
Get = first.get("Name")
print(Get)

print("\n")

# 04.Items()

print("Item")
item = first.items()
print(item)

print("\n")

# 05.Clear()

# print("Clear")
# clr = first.clear()
# print(clr)

print("\n")

# 06.Copy()

print("Copy")
result = first.copy()
print(result)

print("\n")

# 07.Pop()

print("Pop")
value = first.pop("Age")
print(value)


print("\n")

# 08.Update()

print("Update")
first.update({"Age":"30"})
print(first)
