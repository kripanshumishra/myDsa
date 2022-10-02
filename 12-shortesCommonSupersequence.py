b = "gbckd"
a = "agkcdkd"
#agbkcdkd or agkbcdkd 

def scs ( a, b ):
    dp = [0]*(len( a )+1)
    for i in range ( len(dp) ):
        dp[i] = [0] * ( len(b) +1 )

    for i in range ( 1, len(dp) ):
        for j in range ( 1, len(dp[i]) ):
            if ( a[i-1] == b[j-1] ):
                dp[i][j] = dp[i-1][j-1]+1
            else :
                dp[i][ j ] = max ( dp[i-1][j] , dp[ i ][ j-1 ] )
    i , j = len(dp)-1,len(dp[0])-1
    ls=""
    while i>0 and j >0:
        # print(i,j)
        if ( a[i-1] == b [ j-1 ] ):
            ls += a[i-1]
            i-=1
            j-=1
        else :
            if ( dp[i-1][j] > dp[i][j-1] ):
                ls += a[i-1]
                i-=1
            else:
                ls += b[j-1]
                j-=1
    print( i , j  )
    ls =ls[::-1]
    ls= a[:i]+ls[:]
    ls = b[:j]+ls[:]
    print(ls)
        
    return [(len(a)+len(b) - dp[-1][-1]) , ls ]

# print( scs(a,b) )
print( scs("acbbcccaa","bbbcaaaaa") )
#"abcbbcaaaccaa"