a = "akbktcmbmcac"
# input = abac ==> output  == aba

def lpss(a):
    b = a[::-1]
    dp = [0]*(len(a)+1)
    for i in range ( len(dp) ):
        dp[i] = [0]*(len(b)+1)
    for i in range(1, len(dp) ):
        for j in range (1, len(dp[i])):
            if( a[i-1]==b[j-1] ):
                dp[i][j]= dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][ j-1 ])
    i= len(dp)-1
    j= len(dp[0])-1
    ls =""
    while i>0 and j>0:
        if ( a[i-1] == b[j-1] ):
            ls+=a[i-1]
            i-=1
            j-=1
        else:
            if ( dp[i-1][j]>dp[i][j-1] ):
                i-=1
            else:
                j-=1
    print( ls)
    return [dp[-1][-1] , ls[::-1] ]

print(lpss(a))