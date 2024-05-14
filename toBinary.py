n=39
remainders=[]
while n>0:
    remainder=n%2 # remaindenr of devision by 2
    remainders.append(remainder)
    n//2  # we devide n by 2
remainders.reverse()
print(remainders)    