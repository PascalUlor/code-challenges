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