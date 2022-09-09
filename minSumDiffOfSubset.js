// minimise the difference between the subset of array
let arr = [1,11,2,7]

function minDif(arr,sum,arrLen){
    let dp = new Array( arrLen+1 )
    for ( let i=0 ; i< dp.length ; i ++){
        dp[i] = new Array( (sum-sum%2)/2 +1 )
    }

    for ( let i =0 ; i< dp.length; i++ ){
        for ( let j = 0 ; j<dp[i].length;j++ ){
             if( i==0 && j>0 ) dp[i][j] =false
             if ( j==0 ) dp[i][j] = true
        }
    }

    for ( let i=1 ; i<dp.length;i++ ){
        for( let j =1 ; j<dp[i].length;j++ ){
            if( arr[i-1]> j ){
                dp[i][j] = dp[i-1][j]
            }
            
            else {
                dp[i][j] = dp[i-1][j] || dp[i-1][j-arr[i-1]]
            }
        }
    }
    for( let i = 10; i>=0 ; i-- ){
        if ( dp[dp.length-1][i] == true  ) {
            // console.log( dp[dp.length-1][i] )
            // console.log(i)
            return sum - 2*i
        }
    }
    // console.log
    return -1
}
console.log(minDif( arr, 21, 4 ))
console.log(minDif( [1,2,3,4,55], 65, 5 ))