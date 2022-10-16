newA = [0,1,1]
maxi = newA[0]
curr = newA[0]
for i in range (1, len(newA) ):
    if( newA[i] == 1 ):
        curr += 1
    else:
        maxi= max( maxi , curr)
        curr =0 
print( maxi )