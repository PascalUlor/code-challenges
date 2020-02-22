`---Fibonacci---
f(n) = f(n-1) + f(n-2)
for n => Natural numbers
start values:
    f(0) = 0
    f(1) = 1`;
//-------Iterative------//

// const fibonacci = n => {
//   let fibSeq = [0, 1];
//   if (n <= 0) {
//     return [0];
//   }
//   if (n === 1) {
//     return [1];
//   }
//   while (fibSeq.length <= n) {
//     fibSeq.push(fibSeq[fibSeq.length - 1] + fibSeq[fibSeq.length - 2]);
//   }
//   return fibSeq;
// };

//-------Recursive------//
const fibonacci = n => {
    const fib = (loops, list=[0, 1])=> {
        if (loops === 0) {
            list.pop()
            return list
        }
        list1 = list[list.length - 1]
        list2 = list[list.length - 2]
        return fib(loops - 1, [...list, list1 + list2])
    }
    return fib(n-1)
  };
  
console.log(fibonacci(4));


