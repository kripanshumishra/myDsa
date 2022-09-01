// check if string is palindrom or not
const checkPalindrom =(string, start , end)=>{
     if ( end<start ) return true;
     if( !isAlphaNumeric(string[start]) ) return checkPalindrom(string,start+1,end);
     else if( !isAlphaNumeric(string[end]) ) return checkPalindrom(string,start,end-1);

    //  if( string[start]==string[end] ){
    //     return checkPalindrom(string,start+1,end-1)
    //  }
    //  else return false
     return string[start].toLowerCase()===string[end].toLowerCase() && checkPalindrom(string,start+1,end-1);
}
let palaindrom = "Ab@   *^&ba"
console.log(checkPalindrom(palaindrom,0,palaindrom.length-1))


function isAlphaNumeric(char){
   return /[a-z A-Z 0-9]/.test(char) && char != " " ;
}


// console.log(isAlphaNumeric(9))
// console.log(isAlphaNumeric("a"))
// console.log(isAlphaNumeric("A"))
// console.log(isAlphaNumeric("@"))
// console.log(isAlphaNumeric(" "))

