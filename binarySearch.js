const binarySearch = (arr, target, low, high) => {
    if (arr.length === 0) {
      return -1;
    }
  
    let mid = Math.floor((low + high) / 2);
    let guess = arr[mid];
    if (guess === target) {
      return mid;
    }
  
    if (guess < target) {
      return binarySearch(arr, target, mid + 1, high);
    }
    return binarySearch(arr, target, low, mid - 1);
  };
  let arr = [7, 90, 2, 4, 6, 10, 56, 34, 67, 70];
  console.log(binarySearch(arr, 4, 0, arr.length));