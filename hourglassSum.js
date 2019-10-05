const hourglassSum = arr => {
  let maxSum;
  let tempSum;
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      tempSum = 0;
      // top row
      tempSum += arr[i][j];
      tempSum += arr[i][j + 1];
      tempSum += arr[i][j + 2];
      //middle
      tempSum += arr[i + 1][j + 1];
      //bottom row
      tempSum += arr[i + 2][j];
      tempSum += arr[i + 2][j + 1];
      tempSum += arr[i + 2][j + 2];

      //if first hourglass, set as max
      if (tempSum > maxSum || (i == 0 && j == 0)) maxSum = tempSum;
    }
  }
  return maxSum;
};

console.log(
  hourglassSum([
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
  ])
);
