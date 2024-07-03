"""
Set Function

add()
copy()
update()
remove()
clear()
discard()
pop()

"""

print("set")
first = {10,20,30,40,50}
second = {"ram",10,'a',20.10}
print(first)
print(second)

print("\n")

#01.Add

print("add")
first.add(60)
print(first)

print("\n")

#02.Copy

print("Copy")
result = first.copy()
print(result)

print("\n")

#03.Update

print("Update")
first1 = {"ram","sam"}
first.update(first1)
print(first)

print("\n")

#04.Remove

print("Remove")
first.remove(30)
print(first)

print("\n")

#05.Clear

print("clear")
first.clear()
print(first)

print("\n")

#06.Discard

third = {1,2,3,4,5}
print("Discard")
third.discard(3)
print(third)

print("\n")

#07.pop

third = {1,2,3,4,5}
print("Pop")
third.pop()
print(third)

