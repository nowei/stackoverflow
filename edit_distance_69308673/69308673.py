str1="algorithms"
str2="alligator"
m=len(str1)
n=len(str2)

def editdistance(str1, str2, m, n):
  table=[[0 for x in range(n+1)] for x in range(m+1)]
  
  for i in range(m+1):
    for j in range(n+1):

      if i==0:
        table[i][j]=j*20

      elif j==0:
        table[i][j]=i*20

      elif str1[i-1]==str2[j-1]:
        table[i][j]=table[i-1][j-1]

      else:
         table[i][j] = min(20+table[i][j-1], 20+table[i-1][j], 5+table[i-1][j-1])
        

  return table[m][n]

print(editdistance(str1, str2, m, n)) 