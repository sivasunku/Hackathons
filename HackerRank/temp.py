def maxHH(counts):
  a = (list(counts.keys()))
  a.sort(reverse = True)
  DD = D1 = D2 = ''

  for i in a:
    if ( (i<=2) and ( counts[i] > 0 )) :
      D1 = str(i)
      counts[i] -= 1
      break
  for i in a:
    t1 = int(D1 + str(i))
    if ( ( t1 <= 23) and ( counts[i] > 0 ) ):
      D2 = str(i)
      counts[i] -= 1
      break
  DD = D1  + D2
  if ( (DD == '') or (len(DD) != 2) ):
    return "Impossible"
  else:
    return DD

#Months
def maxMM(counts):
  a = (list(counts.keys()))
  a.sort(reverse = True)
  MM = M1 = M2 = ''
  for i in a:
    if ( (i < 6) and (counts[i] > 0 ) ):
      M1 = str(i)
      counts[i] -= 1
      break
  for i in a:
    t = int( M1 + str(i) )
    if ( (t <= 59) and ( counts[i] > 0 ) ) :
      M2 = str(i)
      counts[i] -= 1
      break
  MM=str(M1) + str(M2)
 
  if ( (MM == '') or (len(MM) != 2) ):
    return "Impossible"
  else:
    return MM

def mainFunction(counts):
  bar = ":"
  HH = maxHH(counts)
  
  if ( HH == "Impossible"):
    return(HH)

  MM = maxMM(counts)
  if ( MM == "Impossible"):
    return(MM)
  SS = maxMM(counts)
  if ( SS == "Impossible"):
    return(SS)
  return str(HH) + bar + str(MM) + bar + str(SS)
  
s = "0,0,3,7,7"
#s = "0,0,1,1,3,5,6,7,7"
#s = "3,3,3,3,3,3,3,3,3"
#s = "0,0,0,0,0,1"
counts={0:0,1:0}
inArray = s.split(",")
#inArray = input().split(",")
for i in inArray:
  ele = int(i)
  if ele in counts:
    counts[ele] += 1
  else:
    counts[ele] = 1
print(mainFunction(counts))
