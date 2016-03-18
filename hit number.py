import random
n=random.randint(1,10)
m=int(0)
while int(m) != int(n):
  m=int(input("いくつ??:"))
  if int(m)>int(n):
    print ("それより少ない数です")
  elif int(n)<int(m):
    print ("それより大きい数です")
  else:
    print ("当たりです") 
    break