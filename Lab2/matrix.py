

#Done
def transpose(matrix: list) -> list:
    newlist = []
    if (len(matrix)):
        for i in range(len(matrix[0])):
            list = []
            for ii in range(len(matrix)):
                list.append(matrix[ii][i])
            newlist.append(list)
        return newlist
    else:
        return matrix



#Done
def powers(nums: list, start:int, end:int) -> list :
    lis = []
    for e in nums:
        elist = []
        for pow in range(start,end+1):
            elist.append(e**pow)
        lis.append(elist)
    return lis
            
#Done
def matmul(m1: list, m2:list) -> list:
  m3 = []
  for e1 in m1:
    tempM = []
    for e2 in transpose(m2):
      sum = 0
      for j in range(len(m2)):
        sum += e1[j]*e2[j]
      tempM.append(sum)
    m3.append(tempM)
  return m3
                

#matrix = [[a,b],
#          [c,d]]
#Done
def invert(m: list) -> list:
    a = m[0][0]
    b = m[0][1]
    c = m[1][0]
    d = m[1][1]
    det = a*d-b*c
    lis = [[d/det,-b/det],
           [-c/det,a/det]]
    return lis

#Done
def loadtxt(filename:str) -> list:
    matrix = []
    
    file = open(filename).read().splitlines()
    for line in file:
        linje = line.split()
        newline = []
        for nline in linje:
            newline.append(float(nline))
        matrix.append(newline)

    
    return matrix