function minimumSwaps(arr) {
    let count = 0;
    for ( let i = arr.length - 1; i > 0; i-- ) {
       while ( i+1 != arr[i] ) {
         let temp = arr[arr[i] - 1];
             arr[arr[i] - 1] = arr[i]
             arr[i] = temp;
           count += 1;
       }
    }
    return count
}