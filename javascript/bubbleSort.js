const bubbleSort = (arr) => {
    let noSwap = true;
    for ( let i = arr.length - 1; i > 0; i-- ) {
      noSwap
       for ( let j = 0; j < i; j++ ) {
         if ( arr[j] > arr[j+1]) {
           arr[j] = [arr[j+1], arr[j+1] = arr[j]][0];
           noSwap = false;
         }
       }
      if (noSwap) {
           break;
         }
    }
    return arr
  }