# evaluate string to true boolean paranthesis
string=""
dp = [0]*len(string)
for i in range ( len(dp) ):
    dp[i] = [-1]*len(dp)

def torfDecider ( string ):
    if( string =='T' or string =='t' ):
        return True
    return False


def fun(string , i , j , answer , dp ):
    if( f'{i},{j}' in dp ):
        return dp["{},{}".format(i,j)]
    if ( i==j ):
        # print("this is the gimic" , torfDecider(string[i]) )
        if(torfDecider(string[i])==answer):
            return 1
        return 0
    if( i> j  ):
        return 0

    ansi = 0
    for k in range ( i+1 , j ,2):
        ans=0
        if ( answer ==True ):
            if( string[k] == "|" ):
                leftFalse = fun( string ,i , k-1 , False,dp )
                leftTrue = fun ( string , i, k-1 , True,dp )
                rightTrue = fun( string , k+1 , j ,True ,dp)
                rightFalse = fun ( string , k+1 , j ,False,dp )
                ans += leftFalse*rightTrue + leftTrue*( rightTrue+ rightFalse )
            elif( string[k] == "&" ):
                leftTrue = fun ( string , i, k-1 , True,dp )
                rightTrue = fun( string , k+1 , j ,True,dp )              
                ans += leftTrue*rightTrue
            elif( string[k] == "^" ):
                leftFalse = fun( string ,i , k-1 , False,dp )
                leftTrue = fun ( string , i, k-1 , True,dp )
                rightTrue = fun( string , k+1 , j ,True,dp )
                rightFalse = fun ( string , k+1 , j ,False,dp )
                ans += leftFalse*rightTrue + leftTrue*rightFalse
        else:
            if( string[k] == "&" ):
                leftFalse = fun( string ,i , k-1 , False,dp )
                leftTrue = fun ( string , i, k-1 , True,dp )
                rightTrue = fun( string , k+1 , j ,True,dp )
                rightFalse = fun ( string , k+1 , j ,False,dp )
                ans += leftTrue*rightFalse + leftFalse*( rightTrue+ rightFalse )
            elif( string[k] == "|" ):
                leftFalse = fun ( string , i, k-1 , False,dp )
                rightFalse = fun( string , k+1 , j ,False,dp )              
                ans += leftFalse*rightFalse
            elif( string[k] == "^" ):
                leftFalse = fun( string ,i , k-1 , False,dp )
                leftTrue = fun ( string , i, k-1 , True,dp )
                rightTrue = fun( string , k+1 , j ,True,dp )
                rightFalse = fun ( string , k+1 , j ,False,dp )
                ans += leftFalse*rightFalse + leftTrue*rightTrue
        ansi += ans
    dp['{},{}'.format(i,j)] = ansi
    return ansi
print( fun("T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F" , 0 , 34  , True,{}) )