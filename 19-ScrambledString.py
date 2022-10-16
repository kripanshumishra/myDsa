# def sString(string , i , j ):
#     if( i>=len(string) or j >= len(string) or i>j ):
#         return []
#     if ( i==j ):
#         return [string[i]]
#     ans =[]
#     for k in range( i , j ):
#         localAns =[]
#         left = string[k]
#         right = sString( string , k+1 , j  )
#         for ia in range ( len(left) ):
#             for j in  range( len(right) ):
#                 localAns.append( left[ia]+right[j] )
#                 localAns.append( right[j]+left[ia] )
#         ans += localAns
#     return ans

# print(sString( "great" , 0 , 4  ))

def ss ( string , i , j ):
    # if ( i> len(string)  or i>j ):
    #     return []
    print( i,j )
    if ( i > j ):
        # print('return kar raha hu ans ', i,j ,[])
        return []
    if ( i == j  ):
        # print('return kar raha hu ans ', i,j ,[string[i]])
        return [string[i]]
    ans =[]
    for k in range ( i , j ,1 ):
        # print( k , "this is k for i and j " , i, "and " , j )
        lans =[]
        x = ss( string , i, k )
        y = ss( string , k+1 , j )
        for ia in range ( len(x) ):
            for ja in range ( len(y) ):
                if( x[ia] + y[ja] != y[ja]+ x[ia] ):
                    lans.append( x[ia] + y[ja] )
                    lans.append(  y[ja]+ x[ia]  )
                else:
                    lans.append( x[ia] + y[ja] )
        ans = list(set( ans).union(set(lans) ))
    # print('return kar raha hu ans ', i,j ,ans)
    return ans

print(ss( "abcdefg" , 0, 6))
# print("rgeat")

## detemine whether two strings are scrambled or not 

def sSChecker( a , b ,dp ):
    # print(a,b)
    if(len(a) != len(b)):
        return False
    if( "{}{}".format(a,b) in dp ):
        print("came here")
        dp["{}{}".format(a,b) ]
    if( len(a) == 1 and len( b ) == 1 ):
        dp["{}{}".format(a,b) ] = (a==b)
        return a==b
    ans = False
    for k in range (0,len(a)-1):
        local = False
        left1 = False
        right1 =False
        if( "{}{}".format(a[:k+1] , b[:k+1]) in dp ):
            left1 = dp["{}{}".format(a[:k+1] , b[:k+1])]
        else:
            left1 = sSChecker( a[:k+1] , b[:k+1] ,dp)
        if( left1 ):
            if( "{}{}".format(a[k+1:] , b[k+1:]) in dp ):
                right1 = dp["{}{}".format(a[k+1:] , b[k+1:])]
            else:
                right1 = sSChecker( a[k+1:] , b[k+1:] ,dp)
        
        local = local or ( left1 and right1)
        if(local == False):
            left2 = False
            right2 =False
            if( "{}{}".format(a[:k+1] , b[len(b)-1:len(b)-2-k:-1][::-1] ) in dp ):
                left2 = dp["{}{}".format(a[:k+1] , b[len(b)-1:len(b)-2-k:-1][::-1] )]
            else:
                left2 = sSChecker( a[:k+1] , b[len(b)-1:len(b)-2-k:-1][::-1] ,dp )
            if( left2 ):
                if( "{}{}".format(a[k+1:] , b[:len(b)-k-1]) in dp ):
                    right2 = dp["{}{}".format(a[k+1:] , b[:len(b)-k-1])]
                else:
                    right2 = sSChecker( a[k+1:] , b[:len(b)-k-1] ,dp)
            local = local or (left2 and right2 )
        ans = ans or local
        if( ans ):
            return ans
    dp["{}{}".format(a,b) ] = ans
    return ans

# print(sSChecker( "abcde" , "caebd",{} )) #false
# print(sSChecker( "abcdbdacbdac" , "bdacabcdbdac",{} )) #false

"abcdbdacbdac"
"bdacabcdbdac"