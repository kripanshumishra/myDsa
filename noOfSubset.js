function countSubsetSum (arr,i,j){
    let dp = new Array(i+1)
    for ( let k=0; k<dp.length;k++ ) {
        dp[k] = new Array(j+1)
    }

    for ( let i =0 ; i<dp.length;i++ ){
        for ( let j=0 ; j<dp[i].length;j++ ){
            if( i==0 && j>0 ) dp[i][j]=0
            else if ( j==0 ) dp[i][j]= 1
        }
    }
    for ( let i =1 ; i<dp.length;i++ ){
        for ( let j=1 ; j<dp[i].length;j++ ){
           if( arr[i-1] > j ) dp[i][j] = dp[i-1][ j ]

           else{

            dp[i][j] = dp[i-1][j] + dp[i-1][ j - arr[i-1] ]

           }

        }
    }
    console.log(dp)
    console.log()
    return dp[i][j]
}

console.log(countSubsetSum([2,3,5,6,8,10],6,10))