import math
ka=0
arr=[40, 20, 30, 10, 30]
dp = [math.inf]*len(arr)
for i in range (len(dp)):
    dp[i] = [math.inf]*len(arr)


def mcm ( arr ,i ,j , dp ):
    if ( i>=j  ):
        return 0
    if ( dp[i][j] != math.inf ):
        return dp[i][j]
    ans = math.inf
    for k in range (i, j):
        temp = arr[i-1]*arr[k]*arr[j] + mcm( arr,i , k,dp ) + mcm(arr,k+1 , j ,dp)
        ans = min( temp,ans )
    dp[i][j]= ans
    return ans

print(mcm ( arr ,1,4,dp))
