let arr = [0,1,2,3,4,5,6,7]
let fen = new Array(arr.length).fill(0)
for( let i =1; i<fen.length;i++ ) fenwikUpdate(i,arr[i])
function fenwikUpdate (idx,val){
    while(idx<fen.length){
        fen[idx]+=val
        idx+=(idx & -idx)
    }
}
console.log(fen)
function cal( idx ){
    sum =fen[idx]
    while ( idx &= ~(idx&-idx) ) sum+=fen[idx]
    return sum
}
console.log(cal(4) - cal(1));