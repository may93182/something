a=0
while a<30:
 a=a+1
 if a % 15 == 0:
  print("fizzbuzz")
 elif a/5 == 0:
  print("buzz")
 elif a % 3 == 0:
  print("fizz")
 else:
  print(a)