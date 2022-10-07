import math
str = "abbab"
dp =[0]*len( str )
for i in range ( len(str) ):
    dp[i] = [math.inf]*len(str)


# def isPalindrom(str , i ,j):
#     while i<j:
#         if (str[i]==str[j]):
#             i+=1
#             j-=1
#         else:
#             return False
#     return True

def isPalindrom(s , i ,j):
    str1 = s[i:j+1]
    str2 = str1[::-1]
    return str1 == str2

arr=[]

def pp( str , i , j ,dp ):
    if ( i==j ):
        return 0
    if ( dp[i][j] != math.inf ):
        return dp[i][j]

    if ( isPalindrom( str , i , j ) ):
        return 0
    
    ans = math.inf

    for k in range ( i , j ):
        if ( isPalindrom( str, i,k ) ):
            temp  =  1 + pp( str ,k+1 ,j ,dp )
            ans = min( ans , temp ) 
    
    dp[i][j]= ans

    return ans

print( pp( str , 0 , 4 ,dp) )

