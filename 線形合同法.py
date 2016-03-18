seed1=1
A,B,C=13,1,16

def rand1():
    global seed1,A,B,C
    seed1 = (A*seed1+B)%C
    return seed1
    
for i in range(16):
  print (rand1())