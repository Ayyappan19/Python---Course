"""
Logical
      And &&
	  Or ||
	  Not !
"""

# 01.And

a = 10
b = 20
c = 30
d = 40


result = a < b and c < d   # 10 < 20 and 30 < 40
print("And : ",result )

# OR Gate

result1 = b < c or d < a
print("or",result1)

# Not Gate

result2 = True
print("Not",result2)