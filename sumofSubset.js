let dpArr=new Array(4)
for (let i = 0; i < dpArr.length; i++) {
    dpArr[i] = new Array(6);
}
for(let i =0 ; i<dpArr.length;i++){
    for( let j=0 ; j<dpArr[0].length;j++){

        if(i==0&&j==0) dpArr[i][j] = true
        else{
            if( i==0 && j>0 ) dpArr[i][j] =false
            else if( j==0  ) dpArr[i][j]=true
        }
    }
}
console.log(dpArr)

function isSumSubset(arr,suma){
    for(let len =1 ; len<dpArr.length; len++){
        for ( let sum = 1 ; sum<=suma ; sum++ ){
            if(arr[len-1]>sum ) dpArr[len][ sum ] = dpArr[ len-1 ][ sum ]
            else{
                dpArr[ len ][ sum ] = dpArr[len-1][sum] || dpArr[ len-1 ][ sum- arr[len-1] ]
            }
        }
    }
}
isSumSubset([2,2,3],5)
console.log(dpArr)