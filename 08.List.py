"""
append()
clear()
copy()
count()
extend()
index()
pop()
remove()
reverse()
sort()

"""
#Basic
first = [10,20,30,40,50,30]
print("List : ",first)

second = [10,'a',"ram",10.5]
print("output : ",second)

print("\n")

# 01.Append

print("Append")
first.append(60)
print(first)

print("\n")

# 02.Clear

# print("Clear")
# first.clear()
# print(first)

print("\n")

# 03.Copy

print("Copy")
result = first.copy()
print(result)

print("\n")

# 04.Count

print("Count")
result = first.count(30)
print(result)

print("\n")

# 05.Extend

print("Extend")
first1 = [60,70,80]
first.extend(first1)
print(first)

print("\n")

# 06.Index

print("Index")
third = ["ram","sam","kumar"]
output = third.index("sam")
print(output)

print("\n")

# 07.Insert

print("Insert")
third = ["ram","sam","kumar"]
third.insert(1,"Ayyappan")
print(third)

print("\n")

# 08.Pop

print("Pop")
third = ["ram","sam","kumar"]
third.pop(1)
print(third)

print("\n")

# 09.Remove

print("Remove")
third = ["ram","sam","kumar"]
third.remove("sam")
print(third)

print("\n")

# 10.Reverse

print("Reverse")
third = ["ram","sam","kumar"]
third.reverse()
print(third)

print("\n")

# 11.Sort

print("Sort")
third = ["ram","sam","kumar","anbu"]
third.sort ()
print(third)