let total_num = 5
let val = [15,14,10,45,30]
let wt  = [2 ,5 , 1 ,3 ,4]
let cap = 7
function unboundedKnapsack() {

 const dp = new Array( cap+1 ).fill(0)
 console.log(dp)
 
 for( let i =1 ; i< dp.length ; i++ ){
    for ( let j =0 ; j<wt.length ; j++ ){
        if ( wt[j] <= i ) {
            dp[ i ] = Math.max( dp[i], dp[ i-wt[ j ] ] + val[j] )
            }
        
    }
 }
 
 console.log( dp  )
//  return dp[ dp.length-1 ]

}

unboundedKnapsack()
