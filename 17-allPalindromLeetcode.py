arr = []
def isPalindrom ( s , i, j  ):
    while j<i :
        if ( s[i] == s[j] ):
                i+=1
                j-=1
        else:
            return False
    return True
ans =[]
def all( s , i ,j , arr  ):
    global ans
    if( i>j ):
        ans.append( arr.copy() )
    for k in range ( i , j+1 ):
        if ( isPalindrom( s, i , k  ) ):
            arr.append( s[i:k+1] )
            all( s , k+1 , j , arr )
            arr.pop()
all( "abbab" ,  0 , 4 ,[] )
print( ans  )