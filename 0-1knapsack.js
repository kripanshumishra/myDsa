let total_num = 5
let val = [15,14,10,45,30]
let wt  = [2 ,5 , 1 ,3 ,4]
let cap = 7
function knap (){
    let dp = new Array(wt.length+1)
    for( let i =0 ; i<dp.length; i++ ){
        dp[i]=(new Array(cap+1))
    }
    
    for ( let i = 0 ; i<dp.length ; i++ ){
        for ( let j=0 ; j<dp[i].length ; j++ ){
            if( i===0 || j===0 ) dp[i][j] = 0
        }
    }
    console.log(dp)

    for ( let i = 1 ; i<dp.length ; i++ ){
        for ( let j=1 ; j<dp[i].length ; j++ ){
            if ( wt[i-1]>j ) dp[i][j] = dp[i-1][j]
            else{
                // console.log()
                dp[i][j] = Math.max(dp[i-1][j],dp[i-1][j-wt[i-1]]+val[i-1])
            }
        }
    }
    console.log(dp)
    // return dp[cap+1][cap+1]
}
knap()