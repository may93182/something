def dream():
    M=input()
    N=input()
    ks=[[] for i in range(int(M))]
    for j in range(int(N)):
      while len(ks[j])<int(N):
        ks[j].append(input())
    b=0
    for x in range(int(M)):
      for y in range(int(N)):
         a=int(ks[x][y])
         b=a+b
         a=0
         if b>0:
            c=b
         else:
            b=0
    print(c)