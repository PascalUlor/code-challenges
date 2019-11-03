/*
 * @lc app=leetcode id=200 lang=colavascript
 *
 * [200] Number of Islands
 */

// @lc code=start
/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
  let dimension = grid.length;
  let queue = [];
  let count = 0;
  for (let rowIndex = 0; rowIndex < dimension; rowIndex += 1) {
    for (let colIndex = 0; colIndex < dimension; colIndex += 1) {
        if (grid[rowIndex][colIndex] === '1'){
            queue.push([rowIndex,colIndex]);
            while (queue.length) {
              queue.pop();
              if (grid[rowIndex][colIndex] === '1') {
                  grid[rowIndex][colIndex] = '-1';
                if (
                  rowIndex + 1 >= 0 &&
                  rowIndex + 1< dimension &&
                  colIndex >= 0 &&
                  colIndex < dimension
                ) {
                  return queue.push([rowIndex + 1,colIndex]);
                }
                if (
                  rowIndex - 1 >= 0 &&
                  rowIndex - 1< dimension &&
                  colIndex >= 0 &&
                  colIndex < dimension
                ) {
                  return queue.push([rowIndex - 1,colIndex]);
                }
                if (
                  rowIndex >= 0 &&
                  rowIndex < dimension &&
                  colIndex + 1 >= 0 &&
                  colIndex + 1 < dimension
                ) {
                  return queue.push([rowIndex,colIndex + 1]);
                }
                if (
                  rowIndex >= 0 &&
                  rowIndex < dimension &&
                  colIndex - 1 >= 0 &&
                  colIndex - 1 < dimension
                ) {
                  return queue.push([rowIndex,colIndex - 1]);
                }
              }
            }
            count += 1
        }   
    }
  }
  return count;
};

console.log(
  numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
  ])
);
// @lc code=end
