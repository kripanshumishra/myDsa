const length = [ 1,2,3,4,5 ,6 ,7 ,8 ]
// const price  = [ 1,5,8,9,10,17,17,20]
const price  = [1, 5, 8, 9, 10, 17, 17, 20]
const N =8 
function rod(){
       const  dp = new Array( N+1 ).fill(0) 
    for ( let i =1 ; i<dp.length ; i++ ){
        for (let j =0 ; j<length.length ; j++){
            if( length [ j ] <= i  ) {
                dp[i] = Math.max( dp[i] , dp[i - length[j]] + price[j] )
            }
            else{
                dp[i] = dp[i]
            }
        }
    }

    console.log(dp)
    return dp[ dp.length-1 ]

}
rod()