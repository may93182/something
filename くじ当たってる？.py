def kuji():
    i=0
    U=[input() for i in range(6)]
    N=input()
    kj=[[] for j in range(int(N))]
    for k in range(int(N)):
        if k<int(N):
           while len(kj[k])<6:
              kj[k].append(input())
    z=0
    for r in range(int(N)):
      for g in range(6):
        for y in range(6):
            if U[g] == kj[r][y]:
              z += 1
            else:
              z == z  
      print(z)
      z=0