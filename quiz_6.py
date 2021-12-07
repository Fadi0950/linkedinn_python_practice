def Sum10th(data):
  sum=0
  for i,d in enumerate(data):
    if (i % 10 == 0):
      sum=sum+d
  return sum
data=[1,3,5,7,9,11,13,14,15,17,91,20,21,22,24,26,30,34,36]
print(Sum10th(data))
