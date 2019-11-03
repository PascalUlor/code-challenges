function drawLine(x1, y1, x2, y2):
    # draws line, assume implementation available

function drawHTree(x, y, length, depth):
    # recursion base case
    if (depth == 0):
        return

    x0 = x - length/2
    x1 = x + length/2
    y0 = y - length/2
    y1 = y + length/2

    # draw the 3 line segments of the H-Tree
    drawLine(x0, y0, x0, y1)    # left segment
    drawLine(x1, y0, x1, y1)    # right segment
    drawLine(x0,  y, x1,  y)    # connecting segment

    # at each stage, the length of segments decreases by a factor of √2
    newLength = length/√2

    # decrement depth by 1 and draw an H-tree
    # at each of the tips of the current ‘H’
    drawHTree(x0, y0, newLength, depth-1)     # lower left  H-tree
    drawHTree(x0, y1, newLength, depth-1)     # upper left  H-tree
    drawHTree(x1, y0, newLength, depth-1)     # lower right H-tree
    drawHTree(x1, y1, newLength, depth-1)    
	
	//
	function drawLine(start, end) {
  console.log(`draw line from ${start} to ${end}`);
}

function drawHTree(x, y, length, depth) {
  if (depth === 0) return;
  const midLength = length / 2;
  let leftBottom = [x - midLength, y - midLength];
  let leftTop = [x - midLength, y + midLength];
  let leftCenter = [x - midLength, y];
  let rightBottom = [x + midLength, y - midLength];
  let rightTop = [x + midLength, y + midLength];
  let rightCenter = [x + midLength, y];

  drawLine(rightBottom, rightTop);
  drawLine(leftBottom, leftTop);
  drawLine(leftCenter, rightCenter);
  // draw H Tree
  
  if (depth > 1) {
    const newLength = length / Math.sqrt(2);
    drawHTree( ...rightBottom, newLength, depth - 1);
    drawHTree( ...rightTop, newLength, depth - 1);
    drawHTree( ...leftBottom, newLength, depth - 1);
    drawHTree( ...leftTop, newLength, depth - 1);
  }
}

drawHTree(0, 0, 2, 2);
console.log('Practice makes Perfect!');  

//
Island Count
Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of islands of 1s in binaryMatrix.

An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).

Explain and code the most efficient solution possible and analyze its time and space complexities.

Example:

bfs and dfs
