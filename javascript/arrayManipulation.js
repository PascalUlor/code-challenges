/*
n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
generate an array of zeros from n
loop lines through queries
  -create a loop setting 1st two index as range
  -change index in n-array based on range
*/
// for each sum operation in queries
// update arr with number to add at index=queries[i][0]  and number to remove at index=queries[i][0]+1 =>
// this will allow us to build each element of the final array by summing all elements before it. The aim of this trick is to lower time complexity

// update arr with number to add at index=queries[i][0] 
// and number to remove at index=queries[i][0]+1 => this will allow us to build
// each element of the final array by summing all elements before it. The aim of this trick is to lower time complexity


    function arrayManipulation(n, queries) {
        let nArray = Array(n).fill(0);
          for (let i = 0; i < queries.length; i++) {
            for (let j = queries[i][0]; j <= queries[i][1]; j++) {
                  nArray[j-1] += queries[i][queries[i].length-1]
            }
          }
          return Math.max(...nArray);
        }
        const queries = [[1, 2, 100],
        [2, 5, 100],
        [3, 4, 100]]
        arrayManipulation(5, queries)

// Optimal courtesy Hackerank Discussion
function arrayManipulation(n, queries) {
    let nArray = Array(n).fill(0);
    let max = 0;
      for (let i = 0; i < queries.length; i++) {
              nArray[queries[i][0]-1] += queries[i][queries[i].length-1]
        if(queries[i][1] < nArray.length) {
          nArray[queries[i][1]] -= queries[i][queries[i].length-1]
        }
      }
      for (let j = 1; j < n; j++) {
        nArray[j] += nArray[j-1]
      }
    
      for (let k = 0; k < nArray.length; k++) {
        max = Math.max(max, nArray[k]);
      }
    return max;
    }