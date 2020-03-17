function rotateImage(arr) {
    // return arr.map((_,i,origin) => origin.map(a => a[i])).reverse()
    let newArr =[]
    let result =[]
    for(let i=0; i<arr.length; i++){
      for(let j=0; j<arr.length; j++){
         newArr.push(arr[j][i]);
      }
    }
    for(let k = 0; k<newArr.length; k+=arr.length){
      result.push(newArr.slice(k,k+arr.length));
    }
    return result.reverse();
    
    }
    
    rotateImage([
      [1, 1, 5, 9, 9],
      [2, 2, 6, 0, 0],
      [3, 3, 7, 1, 1],
      [4, 4, 8, 2, 2],
      [5, 5, 9, 3, 3]
      ])