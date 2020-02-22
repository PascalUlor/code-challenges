function isBalanced(s) {
    start_timer
    const bracketArr = s.split('')
     const cacheBracket = {
         '{':'}',
         '[': ']',
         '(': ')'
     }
     const arrStore = []
     for (let i = 0; i< bracketArr.length; i++) {
         if(bracketArr[i] === '{' || bracketArr[i] === '[' || bracketArr[i] === '(') {
             arrStore.push(bracketArr[i])
         } else {
             const oppBracket = arrStore.pop()
             if(bracketArr[i] !== cacheBracket[oppBracket] ) {
                return 'NO'
             }
         }
     }
     if(arrStore.length) {
         return 'NO'
     }
     return 'YES'
    }
const start_timer = new Date().getTime().toString()
const end_timer = new Date().getTime().toString()
console.log(start_timer)
console.log(isBalanced('{[()]}'))
console.log(isBalanced('{[(])}'))
console.log(isBalanced('{(([])[])[]}[]'))
console.log(isBalanced('{(([])[])[]}'))
console.log(end_timer)
console.log(end_timer-start_timer)



function balancedBrackets(string) {
    // create an bracketArray from sting of brackets
 const bracketArray = string.split('');
// create a cache of all open bracket as keys and closing brackets as values
const cache = {
    '{':'}',
    '[': ']',
    '(': ')',
    '|': '|'
};
// loop through bracketArr and store opening bracket in an openBracket
const openBracket = [];
 for (let i = 0; i < bracketArray.length; i++) {
     if (bracketArray[i] === '{' || bracketArray[i] === '[' || bracketArray[i] === '(') {
         openBracket.push(bracketArray[i]);
     } else if (bracketArray[i] === '|') {
         if (openBracket[openBracket.length - 1] === '|') {
            openBracket.pop()
         }
         openBracket.push(bracketArray[i]); 
     } 
     else if (bracketArray[i] === '}' || bracketArray[i] === ']' || bracketArray[i] === ')') {
         // if not opening bracket pop and compare last push open bracket
         if (openBracket[openBracket.length - 1] === '|') {
            openBracket.pop()
         }
         const closeBracket = openBracket.pop();
         console.log(openBracket)
        if (bracketArray[i] !== cache[closeBracket]) {
            return 0;
        }
     }
 }