a = "aabebcdd"
# output => abd is the longest repeating subsequence 
def lpss (a):
    b = a
    dp = [0]*(len(a)+1)
    for i in range (len(dp)):
        dp[i] = [0]*(len(b)+1)
    for i in range ( 1,len(dp) ):
        for j in range ( 1, len(dp[i]) ):
            if( j != i ):
                if ( a[ i-1 ] == b[ j-1 ] ):
                    dp[i][j] = 1+ dp[i-1][j-1]
                else:
                    dp[i][j] = max( dp[i-1][j] , dp[i][ j-1 ] )  
            else:
                dp[i][j] = max( dp[i-1][j] , dp[i][ j-1 ] )   
    i , j = len(dp)-1 , len(dp[0])-1
    ls =""
    while  i > 0 and j >0 :
        if ( i != j  ):
            if ( a[i-1] ==  b[j-1] ):
                ls+=a[i-1]
                i-=1
                j-=1
            elif ( dp[i-1][j] > dp[i][j-1] ):
                i-=1
            else:
                j-=1
        else:
            if ( dp[i-1][j] > dp[i][j-1] ):
                i-=1
            else:
                j-=1
    print(ls) 
    return (dp[-1][-1])
print(lpss(a))