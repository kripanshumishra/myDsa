// we have to find min no. of coins to make sum if possible 

// coins =[1,2,5], target = 11 
//output => 3 coins =>{5,5,1}


//##########################   RECURSION    #############################################

const coins =[1,2,3]
const target = 6
let m ={}

function minCoin(target,m){
    if( target in m ) return m[target]
    if( target===0 ) return 0
    if( target<0 ) return Infinity
    let min= Infinity
    for( let i =0 ; i< coins.length; i++ ){
        if( target>=coins[i] ) {
            let mid = 1 + minCoin(target-coins[i],m)
            if( mid<min ) min=mid
            // console.log( mid )
        }

    }
    m[target]= min
    return min
}

function maxCoinAngshu( target , i ){
    if( target===0  ) return 0
    if( target<0 || i>= coins.length ) return Infinity
    let a = 1+ maxCoinAngshu( target-coins[i] , i+1 )
    let b = maxCoinAngshu( target , i+1 )
    let c = 1+maxCoinAngshu( target-coins[i] ,i )
    return Math.min( a,b,c )
}

console.log(minCoin( target,m ))
console.log( maxCoinAngshu( target,0 ))
