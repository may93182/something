def fibonacci(x):
  if x==1:
    return 1
  elif x==2:
    return 1
  else:
    return fibonacci(x-1)+fibonacci(x-2)
    
print (fibonacci(a))