# Que => min no of insertion or deletion to make string palindrom 
# app => len(string) - len( lcs with reversed array  )

from re import A


a = "abckdcba"
# b = "abcdkcba"

def counter (a):
    b = a[::-1]
    dp = [0]*(len(a)+1)
    for i in range (len(dp)):
        dp[i] = [0]*(len(b)+1)
    for i in range ( 1,len(dp) ):
        for j in range ( 1, len(dp[i]) ):
            if ( a[ i-1 ] == b[ j-1 ] ):
                dp[i][j] = 1+ dp[i-1][j-1]
            else:
                dp[i][j] = max( dp[i-1][j] , dp[i][ j-1 ] )    
    return (len(a)-dp[-1][-1])
print(counter(a))
print(counter("zzazz")) #0