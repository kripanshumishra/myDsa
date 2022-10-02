const coin = [ 1,2,3 ]
const sum = 6
function coinChange(  ){

    const dp = new Array( sum+1 ).fill(0)
    dp[0] =1
    
    // for ( let i=1 ; i<dp.length ; i++ ){
    //     for( let j =0 ; j<coin.length; j++ ) {
    //         if( coin[j]<= i ){         
    //             if( dp[i-coin[j]]!=0 ) dp[i] = dp[i] + dp[ i-coin[j] ];
    //             else dp[i] = dp[i]
    //         }
    //         else{
    //             dp[i] = dp[i]
    //         }
    //     }
    // }

    for ( let j =0 ; j< coin.length ; j++ ){
        for ( let i=0 ; i<dp.length ; i++ ){
            if( coin[ j ] <= i ){
                dp[ i ] = dp[ i ]+ dp[ i-coin[j] ]
            }
            
        }
        
    }
    console.log(dp)
    return dp[dp.length-1]
}
function minNoCoinChange(  ){

    const dp = new Array( sum+1 ).fill(1000000000)
    dp[0] =1
    
    // for ( let i=1 ; i<dp.length ; i++ ){
    //     for( let j =0 ; j<coin.length; j++ ) {
    //         if( coin[j]<= i ){
                
    //             if( dp[i-coin[j]]!=0 ) dp[i] = dp[i] + dp[ i-coin[j] ];
    //             else dp[i] = dp[i]
    //         }
    //         else{
    //             dp[i] = dp[i]
    //         }
    //     }
    // }

    for ( let j =0 ; j< coin.length ; j++ ){
        for ( let i=0 ; i<dp.length ; i++ ){
            if( coin[ j ] <= i ){
                dp[ i ] = Math.min(dp[ i ], dp[ i-coin[j]])
            }
        }
        
    }
    console.log(dp)
    return dp[dp.length-1]
}

coinChange()
// minNoCoinChange()
