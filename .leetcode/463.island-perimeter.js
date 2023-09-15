/*
 * @lc app=leetcode id=463 lang=javascript
 *
 * [463] Island Perimeter
 *
 * https://leetcode.com/problems/island-perimeter/description/
 *
 * algorithms
 * Easy (69.66%)
 * Likes:    5401
 * Dislikes: 265
 * Total Accepted:    421.3K
 * Total Submissions: 604.8K
 * Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
 *
 * You are given row x col grid representing a map where grid[i][j] = 1
 * represents land and grid[i][j] = 0 represents water.
 * 
 * Grid cells are connected horizontally/vertically (not diagonally). The grid
 * is completely surrounded by water, and there is exactly one island (i.e.,
 * one or more connected land cells).
 * 
 * The island doesn't have "lakes", meaning the water inside isn't connected to
 * the water around the island. One cell is a square with side length 1. The
 * grid is rectangular, width and height don't exceed 100. Determine the
 * perimeter of the island.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
 * Output: 16
 * Explanation: The perimeter is the 16 yellow stripes in the image above.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: grid = [[1]]
 * Output: 4
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: grid = [[1,0]]
 * Output: 4
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * row == grid.length
 * col == grid[i].length
 * 1 <= row, col <= 100
 * grid[i][j] is 0 or 1.
 * There is exactly one island in grid.
 * 
 * 
 */

// @lc code=start

// class Queues {
//     constructor(){
//         this.queue = [];
//     }
//     enqueue(value) {
//         return this.queue.push(value);
//     }
//     dequeue() {
//         if(this.size()) {
//         return this.queue.pop(0);
//         }
//         return 0;
//     }
//     size() {
//         return this.queue.length;
//     }
// }

/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    let rows = grid.length;
    let cols = grid[0].length;
    let perimeter = 0;
    // let queue = new Queues();

    for (let rowIndex = 0; rowIndex < rows; rowIndex+=1) {
        for (let colIndex = 0; colIndex < cols; colIndex+=1) {
            // queue.enqueue([rowIndex, colIndex]);
            if(grid[rowIndex][colIndex] === 1) {
                perimeter += 4;
                if((rowIndex - 1 >= 0 && rowIndex - 1 < rows) && (colIndex >= 0 && colIndex < cols) && grid[rowIndex - 1][colIndex] === 1) {
                    perimeter -= 1;
                }
                if((rowIndex + 1 >= 0 && rowIndex + 1 < rows) && (colIndex >= 0 && colIndex < cols) && grid[rowIndex + 1][colIndex] === 1) {
                    perimeter -= 1;
                }
                if((rowIndex >= 0 && rowIndex < rows) && (colIndex - 1 >= 0 && colIndex - 1 < cols) && grid[rowIndex][colIndex - 1] === 1) {
                    perimeter -= 1;
                }
                if((rowIndex >= 0 && rowIndex < rows) && (colIndex + 1 >= 0 && colIndex + 1 < cols) && grid[rowIndex][colIndex + 1] === 1) {
                    perimeter -= 1;
                }
                // while (queue.length) {
                //     let currentNode = queue.dequeue();
                //     let rx = currentNode[0];
                //     let cy = currentNode[1];
                //     if(grid[rx][cy] === 1) {
                //         grid[rx][cy] = 0;
                //         if((rx + 1 >= 0 && rx + 1 < rows) && (cy >= 0 && cy < cols)) {
                //             queue.enqueue([rx + 1, cy]);
                //         }
                //         if((rx - 1 >= 0 && rx - 1 < rows) && (cy >= 0 && cy < cols)) {
                //             queue.enqueue([rx - 1, cy]);
                //         }
                //         if((rx >= 0 && rx < rows) && (cy + 1 >= 0 && cy + 1 < cols)) {
                //             queue.enqueue([rx, cy + 1]);
                //         }
                //         if((rx >= 0 && rx < rows) && (cy - 1 >= 0 && cy - 1 < cols)) {
                //             queue.enqueue([rx, cy - 1]);
                //         }
                //     }
                // }
            }
            
        }
    }
    return perimeter;
    
};

// @lc code=end

