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
  let rowDimension = grid.length;
  let colDimension = grid[0] !== undefined ? grid[0].length : grid.length;
  let queue = [];
  let visited = [];
  let count = 0;
  for (let rowIndex = 0; rowIndex < rowDimension; rowIndex += 1) {
    for (let colIndex = 0; colIndex < colDimension; colIndex += 1) {
      if (grid[rowIndex][colIndex] === "1") {
        queue.push([rowIndex, colIndex]);
        while (queue.length) {
          let currentNode = queue.pop();
          visited.push(grid[currentNode[0]][currentNode[1]]);
          let rx = currentNode[0];
          let cy = currentNode[1];
          if (grid[rx][cy] === "1") {
            grid[rx][cy] = "-1";
            if (
              rx + 1 >= 0 &&
              rx + 1 < rowDimension &&
              cy >= 0 &&
              cy < colDimension
            ) {
              queue.push([rx + 1, cy]);
            }
            if (
              rx - 1 >= 0 &&
              rx - 1 < rowDimension &&
              cy >= 0 &&
              cy < colDimension
            ) {
              queue.push([rx - 1, cy]);
            }
            if (
              rx >= 0 &&
              rx < rowDimension &&
              cy + 1 >= 0 &&
              cy + 1 < colDimension
            ) {
              queue.push([rx, cy + 1]);
            }
            if (
              rx >= 0 &&
              rx < rowDimension &&
              cy - 1 >= 0 &&
              cy - 1 < colDimension
            ) {
              queue.push([rx, cy - 1]);
            }
          }
        }
        count += 1;
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

console.log(
  numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
  ])
);

console.log(numIslands([["1", "0", "1", "1", "0", "1", "1"]]));
// @lc code=end
